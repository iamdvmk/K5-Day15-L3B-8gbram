"""Công cụ chỉ đọc cho bản demo tin nhắn tài chính."""

import csv
import re
import unicodedata
from pathlib import Path
from urllib.parse import urlsplit

from tracing import tool

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def _plain(text: str) -> str:
    text = unicodedata.normalize("NFD", text.lower())
    return "".join(ch for ch in text if unicodedata.category(ch) != "Mn").replace("đ", "d")


def _link_and_host(text: str) -> tuple[str, str, bool]:
    """Lấy host thực của URL; phần trước @ không được tính là host chính thức."""
    text = text.translate(str.maketrans({"．": ".", "。": ".", "｡": "."}))
    url = re.search(r"(?i)https?://[^\s]+", text)
    if url:
        raw = url.group(0).rstrip(".,;)")
        parsed = urlsplit(raw)
        return raw, (parsed.hostname or "").lower(), parsed.username is not None
    bare = re.search(r"(?i)\b[a-z][a-z0-9-]*(?:\.[a-z0-9-]+)*\.(?:com(?:\.vn)?|vn|top|cc|info|vip|net|org|ly|xyz|online|shop|asia)\b", text)
    return (bare.group(0), bare.group(0).lower(), False) if bare else ("", "", False)


@tool
def tra_ten_mien(link: str) -> str:
    """Tra tên miền. Input: link/host. Output: trạng thái trong hai CSV. Không tác động ra ngoài."""
    _, host, has_userinfo = _link_and_host(link.replace("[.]", "."))
    host = host.removeprefix("www.")
    if not host or has_userinfo:
        return "không có trong dữ liệu"
    for filename, status in (("ten_mien_lua_dao.csv", "đã bị báo cáo lừa đảo"),
                             ("ten_mien_ngan_hang.csv", "tên miền chính thức")):
        path = DATA_DIR / filename
        if not path.exists():
            continue
        with path.open(encoding="utf-8-sig", newline="") as stream:
            for row in csv.DictReader(stream):
                value = (row.get("ten_mien") or "").strip().replace("[.]", ".")
                parsed = urlsplit(value if "://" in value else "https://" + value)
                listed_host, listed_userinfo = (parsed.hostname or "").lower(), parsed.username is not None
                listed_host = listed_host.removeprefix("www.")
                if listed_host and not listed_userinfo and (host == listed_host or host.endswith("." + listed_host)):
                    return status
    return "không có trong dữ liệu"


def redact_secrets(text: str) -> str:
    """Che OTP, mật khẩu, SĐT và STK có nhãn trước khi ghi trace hoặc gọi model."""
    text = re.sub(r"(?i)(\b(?:otp|ma xac thuc|mã xác thực)\b[^\d\n]{0,60}?)\b\d(?:[ .-]?\d){3,7}\b", r"\1[ĐÃ CHE]", text)
    text = re.sub(r"(?i)(\b(?:mat khau|mật khẩu|password)\b\s*(?:la|là|:)?\s*)\S+", r"\1[ĐÃ CHE]", text)
    # STK không có một độ dài chung cho mọi ngân hàng: chỉ che chuỗi 6–19 chữ số
    # khi có nhãn tài khoản ngay trước nó; giữ nguyên tiền, ngày và hotline.
    text = re.sub(
        r"(?i)(\b(?:stk|số tài khoản|so tai khoan|tài khoản số|tai khoan so|tk)\b\s*(?:[a-z]{2,25}\s*)?(?::|là|la|số|so)?\s*)(\d(?:[ .-]?\d){5,18})(?!\w)",
        r"\1[ĐÃ CHE STK]", text,
    )
    text = re.sub(
        r"(?i)(\b(?:chuyển khoản|chuyen khoan|chuyển tiền|chuyen tien|gửi tiền|gui tien)\b[^\d\n]{0,50}?\b(?:vào|vao|đến|den|cho)\b\s*(?:(?:số|so|stk|tk|tài khoản|tai khoan)\s*)?)(\d(?:[ .-]?\d){5,18})(?!\w)",
        r"\1[ĐÃ CHE STK]", text,
    )
    return re.sub(r"(?<!\w)(?:\+84|0)[ .-]?[35789](?:[ .-]?\d){8}(?!\w)", "[ĐÃ CHE SĐT]", text)


def _inspect_single(text: str) -> dict:
    """Rút dấu hiệu cho một URL; không ghi thêm sự kiện tool vào trace."""
    plain = _plain(text)
    flags = []
    link, host, has_userinfo = _link_and_host(text.replace("[.]", "."))
    has_link = bool(link)
    host = host.removeprefix("www.")
    domain_status = tra_ten_mien(link) if has_link else "không có trong dữ liệu"
    official_host = domain_status == "tên miền chính thức"
    action_text = re.sub(r"\bkhong gui link dang nhap\b", "", plain)
    asks_action = bool(re.search(r"\b(?:bam|truy cap|dang nhap|nhap|cung cap|doc giup|tai file|cai dat|chuyen tien|nop tien|doi qua|huy|tra cuu|xac thuc)\b", action_text))
    otp = bool(re.search(r"\botp\b|ma xac thuc|mat khau", plain))
    requests_secret = otp and bool(re.search(r"\b(?:doc giup|nhap|gui|cung cap)(?:\s+\w+){0,3}\s+(?:ma\s+)?(?:otp|xac thuc|xac nhan|mat khau)\b", plain)) and not bool(re.search(r"\b(?:khong|tuyet doi khong) cung cap\b", plain))
    urgency = bool(re.search(r"\b(?:ngay|gap|trong \d+ phut|sau \d+ gio|hom nay|vinh vien|truoc \d+ ?h)\b", plain))
    money = bool(re.search(r"\b(?:chuyen tien|chuyen giup|nop tien|thanh toan|vay tien)\b", plain))
    if has_link and asks_action and not official_host:
        flags.append("Có link kèm yêu cầu thao tác: " + host)
    if has_userinfo:
        flags.append("URL chứa dấu @; tên miền trước @ không phải địa chỉ đích")
    if domain_status == "đã bị báo cáo lừa đảo":
        flags.append("Tên miền đã bị báo cáo lừa đảo: " + host)
    if has_link and host == "bit.ly":
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
    risk = "Cao" if has_userinfo or (domain_status == "đã bị báo cáo lừa đảo") or (has_link and asks_action and not official_host) or requests_secret or (money and urgency) or ("mat khau" in plain and "[da che]" in plain) else "Trung bình" if flags or (has_link and not official_host) else "Thấp"
    return {"risk": risk, "red_flags": flags}


@tool
def inspect_message(text: str) -> dict:
    """Rút dấu hiệu. Input: tin đã che. Output: mức rủi ro quy tắc và dấu hiệu. Không tác động ra ngoài."""
    normalized = text.replace("[.]", ".")
    urls = re.findall(r"(?i)https?://[^\s]+", normalized)
    if len(urls) <= 1:
        return _inspect_single(normalized)

    context = normalized
    for url in urls:
        context = context.replace(url, "", 1)
    findings = {"risk": "Thấp", "red_flags": []}
    for url in urls:
        candidate = _inspect_single(context + " " + url)
        if candidate["risk"] == "Cao":
            findings["risk"] = "Cao"
        elif candidate["risk"] == "Trung bình" and findings["risk"] != "Cao":
            findings["risk"] = "Trung bình"
        findings["red_flags"].extend(candidate["red_flags"])
    findings["red_flags"] = list(dict.fromkeys(findings["red_flags"]))
    return findings
