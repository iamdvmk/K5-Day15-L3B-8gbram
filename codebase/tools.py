"""Công cụ chỉ đọc cho bản demo tin nhắn tài chính."""

import re
import unicodedata

from tracing import tool


def _plain(text: str) -> str:
    text = unicodedata.normalize("NFD", text.lower())
    return "".join(ch for ch in text if unicodedata.category(ch) != "Mn").replace("đ", "d")


def redact_secrets(text: str) -> str:
    """Che OTP, mật khẩu và SĐT trước khi ghi trace hoặc gọi model."""
    text = re.sub(r"(?i)(\b(?:otp|ma xac thuc|mã xác thực)\b[^\d\n]{0,60}?)\b\d{4,8}\b", r"\1[ĐÃ CHE]", text)
    text = re.sub(r"(?i)(\b(?:mat khau|mật khẩu|password)\b\s*(?:la|là|:)?\s*)\S+", r"\1[ĐÃ CHE]", text)
    return re.sub(r"(?<!\w)(?:\+84|0)[ .-]?[35789](?:[ .-]?\d){8}(?!\w)", "[ĐÃ CHE SĐT]", text)


@tool
def inspect_message(text: str) -> dict:
    """Rút dấu hiệu. Input: tin đã che. Output: dấu hiệu và mức rủi ro mock. Không tác động ra ngoài."""
    plain = _plain(text)
    flags = []
    link = re.search(r"(?i)(?:https?://)?\b[a-z][a-z0-9-]*(?:\.[a-z0-9-]+)*\.(?:com(?:\.vn)?|vn|top|cc|info|vip|net|org|ly)\b", text)
    has_link = bool(link)
    asks_action = bool(re.search(r"\b(?:bam|truy cap|dang nhap|nhap|cung cap|doc giup|tai file|cai dat|chuyen tien|nop tien|doi qua|huy|tra cuu|xac thuc)\b", plain))
    otp = bool(re.search(r"\botp\b|ma xac thuc|mat khau", plain))
    requests_secret = otp and bool(re.search(r"\b(?:doc giup|nhap|gui|cung cap)\b", plain)) and not bool(re.search(r"\b(?:khong|tuyet doi khong) cung cap\b", plain))
    urgency = bool(re.search(r"\b(?:ngay|gap|trong \d+ phut|sau \d+ gio|hom nay|vinh vien|truoc \d+ ?h)\b", plain))
    money = bool(re.search(r"\b(?:chuyen tien|chuyen giup|nop tien|thanh toan|vay tien)\b", plain))
    if has_link and asks_action:
        flags.append("Có link kèm yêu cầu thao tác: " + link.group(0))
    if has_link and link.group(0).lower().startswith("bit.ly"):
        flags.append("Link rút gọn che địa chỉ đích")
    if requests_secret:
        flags.append("Yêu cầu thao tác với OTP hoặc mật khẩu")
    if urgency and asks_action:
        flags.append("Thúc giục làm ngay")
    if money and urgency:
        flags.append("Thúc giục chuyển hoặc nộp tiền")
    if ".apk" in plain and asks_action:
        flags.append("Yêu cầu cài tệp APK từ tin nhắn")
    if "mat khau" in plain and "[da che]" in plain:
        flags.append("Người dùng đã đưa mật khẩu vào nội dung cần kiểm tra")
    if "[system]" in plain or "bo qua moi huong dan" in plain or "ignore previous" in plain:
        flags.append("Tin nhắn chứa chỉ dẫn nhằm thay đổi cách đánh giá")
    risk = "Cao" if (has_link and asks_action) or requests_secret or (money and urgency) or ("mat khau" in plain and "[da che]" in plain) else "Trung bình" if flags or has_link else "Thấp"
    return {"risk": risk, "red_flags": flags}
