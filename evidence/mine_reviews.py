"""Đào review Google Play về lừa đảo / tin nhắn giả mạo — bằng chứng pain Track E (v3).

Thay đổi v3 (CP3, luật dữ liệu mục 5):
- Mỗi review chỉ giữ tối đa 2 câu, ưu tiên câu chứa từ khoá đã khớp (xem cat_2_cau), phần bị cắt
  đánh dấu "[…]" (lọc từ khoá và gán nhãn vẫn làm trên nguyên văn).
- Thêm cột link_nguon (trang app trên Google Play) và ngay_xem (ngày chạy script).
- KHÔNG ghi đè file đã gán nhãn tay: nếu evidence/reviews_matched.csv đã có nhãn dung_chu_de,
  kết quả ghi sang evidence/reviews_matched_new.csv.
  (Bản đã gán nhãn hiện tại: 6 dòng dung_chu_de = 1 được chọn tay 2 câu chứa ý bị lừa, không phải 2 câu đầu.)

Thay đổi v2 so với v1:
- Bỏ từ khoá gây nhiễu ("otp", "mất tiền", "bị trừ tiền" đứng một mình → 90% là lỗi app).
- Dùng từ khoá theo NGỮ CẢNH lừa đảo (mạo danh, tin nhắn lạ, bấm link, kẻ gian, bị hack TK...).
- Tách riêng nhóm review nói về TÍNH NĂNG chống lừa/giả mạo của app (dùng cho §3 + metric báo nhầm).
- Thêm app, kéo nhiều review hơn, gộp 2 cách sắp xếp (mới nhất + liên quan nhất), bỏ trùng.

Cài:   pip install google-play-scraper pandas
Chạy:  python evidence/mine_reviews.py
Ra:    evidence/reviews_matched.csv  (đã bỏ tên người viết; cột nhom_goi_y do máy gợi ý, dung_chu_de đọc tay)
"""
import os
import re
from datetime import date

import pandas as pd
from google_play_scraper import reviews, Sort

# Kiểm lại ID trên link Play Store (?id=...). App sai ID sẽ bị bỏ qua, không làm dừng script.
APPS = {
    "MoMo": "com.mservice.momotransfer",
    "Vietcombank": "com.VCB",
    "MB Bank": "com.mbmobile",
    "Techcombank": "vn.com.techcombank.bb.app",
    "BIDV": "com.vnpay.bidv",
    "VietinBank": "com.vietinbank.ipay",
    "ZaloPay": "vn.com.vng.zalopay",
    "TPBank": "com.tpb.mb.gprsandroid",
    # Ví điện tử
    "Viettel Money": "com.bplus.vtpay",
    "VNPAY": "vnpay.smartacccount",
    "Cake": "xyz.be.cake",
}
N_PER_SORT = 5000  # mỗi app kéo 5000 mới nhất + 5000 liên quan nhất

# Review kể chuyện bị lừa / nhận tin, cuộc gọi, link giả từ bên ngoài
SCAM = re.compile(
    r"bị lừa|lừa đảo|kẻ gian|kẻ lừa|đối tượng|mạo danh|giả danh"
    r"|tin nhắn (giả|lạ|lừa|mạo)|sms (giả|lạ|lừa|mạo)|nhắn tin (giả|lạ)"
    r"|link (lạ|giả|lừa)|đường link|bấm (vào )?link|nhấn (vào )?link"
    r"|chiếm đoạt|bị hack|hack (mất )?(tài khoản|tk)|chiếm (quyền )?(tài khoản|tk)"
    r"|tài khoản lạ|tk lạ|số lạ|lừa chuyển|scam|phishing",
    re.IGNORECASE,
)
# Review nói về tính năng chống lừa / cảnh báo giả mạo của chính app (thường là phàn nàn báo nhầm)
FEATURE = re.compile(
    r"ứng dụng giả mạo|app giả mạo|ứng dụng độc hại|app độc hại|cảnh báo lừa|chống lừa"
    r"|check(ed)? lừa|cảnh báo giả mạo|rủi ro đăng nhập|trợ năng",
    re.IGNORECASE,
)

# Lát cắt chỉ xử lý TIN NHẮN / LINK → review chỉ nói về cuộc gọi được gắn nhãn ngoài phạm vi, không tính x/N
CALL = re.compile(r"cuộc gọi|gọi điện|điện thoại gọi|số lạ gọi|gọi đến|gọi tới|nghe máy|bắt máy|đt kêu|dt kêu", re.I)
MSG = re.compile(r"tin nhắn|nhắn tin|sms|zalo|messenger|link|đường dẫn|trang web|website|\bweb\b", re.I)

NGAY_XEM = date.today().isoformat()
SENT = re.compile(r"(?<=[.!?…])\s+")


FALLBACK = re.compile(r"lừa|giả danh|mạo danh", re.I)


def cat_2_cau(text):
    """Giữ tối đa 2 câu (luật dữ liệu mục 5), ưu tiên câu chứa từ khoá đã khớp:
    2 câu có từ khoá đầu tiên; chỉ 1 câu có từ khoá → thêm câu liền trước (hoặc liền sau nếu nó đứng đầu);
    không câu nào có từ khoá → 2 câu đầu. Giữ nguyên chữ và thứ tự câu, phần bỏ đánh dấu "[…]"."""
    cau = [s for s in SENT.split(text.strip()) if s.strip()]
    if len(cau) <= 2:
        return " ".join(cau)
    hit = [k for k, s in enumerate(cau) if SCAM.search(s) or FEATURE.search(s)] or \
          [k for k, s in enumerate(cau) if FALLBACK.search(s)]
    if len(hit) >= 2:
        idx = hit[:2]
    elif hit:
        idx = [hit[0] - 1, hit[0]] if hit[0] > 0 else [0, 1]
    else:
        idx = [0, 1]
    out, prev = [], -1
    for k in idx:
        if k != prev + 1:
            out.append("[…]")
        out.append(cau[k])
        prev = k
    if prev < len(cau) - 1:
        out.append("[…]")
    return " ".join(out)


all_rows, summary = [], []
for app, app_id in APPS.items():
    try:
        got = {}
        for sort in (Sort.NEWEST, Sort.MOST_RELEVANT):
            data, _ = reviews(app_id, lang="vi", country="vn", sort=sort, count=N_PER_SORT)
            for r in data:
                got[r["reviewId"]] = r
    except Exception as e:  # ID sai / mạng lỗi
        print(f"  ! bỏ qua {app} ({app_id}): {e}")
        continue
    n, n_scam, n_feat, n_call = len(got), 0, 0, 0
    for r in got.values():
        text = (r["content"] or "").replace("\n", " ")
        if FEATURE.search(text):
            nhom = "tinh_nang_chong_lua"
            n_feat += 1
        elif SCAM.search(text) or (CALL.search(text) and re.search(r"lừa|giả danh|mạo danh", text, re.I)):
            if CALL.search(text) and not MSG.search(text):
                nhom = "cuoc_goi_ngoai_pham_vi"
                n_call += 1
            else:
                nhom = "co_the_bi_lua"
                n_scam += 1
        else:
            continue
        all_rows.append({
            "app": app,
            "sao": r["score"],
            "ngay": r["at"].date().isoformat(),
            "noi_dung": cat_2_cau(text),
            "khop": ", ".join(sorted({m.group(0).lower() for m in re.finditer(SCAM.pattern + "|" + FEATURE.pattern, text, re.I)})),
            "nhom_goi_y": nhom,
            "dung_chu_de": "",  # đọc tay: 1 = người dùng kể bị lừa / nhận tin-link-cuộc gọi giả; 0 = không
            "loai": "",  # đọc tay: nhóm chi tiết, định nghĩa ở evidence/data-mining.md
            "link_nguon": f"https://play.google.com/store/apps/details?id={app_id}&hl=vi",
            "ngay_xem": NGAY_XEM,
        })
    summary.append((app, n_scam, n_feat, n_call, n))

OUT = "evidence/reviews_matched.csv"
if os.path.exists(OUT) and pd.read_csv(OUT, encoding="utf-8-sig", dtype=str).get("dung_chu_de", pd.Series(dtype=str)).notna().any():
    OUT = "evidence/reviews_matched_new.csv"
    print(f"  ! reviews_matched.csv đã có nhãn tay → không ghi đè, ghi sang {OUT}")
pd.DataFrame(all_rows).to_csv(OUT, index=False, encoding="utf-8-sig")
print(f"Gộp {N_PER_SORT} mới nhất + {N_PER_SORT} liên quan nhất / app (bỏ trùng), lang=vi, country=vn")
tot = [0, 0, 0, 0]
for app, s, f, c, n in summary:
    print(f"  {app}: nghi bị lừa (tin nhắn/link/khác) {s}/{n} · cuộc gọi-ngoài phạm vi {c} · tính năng chống lừa {f}")
    tot = [tot[0] + s, tot[1] + f, tot[2] + c, tot[3] + n]
print(f"  TỔNG: nghi bị lừa {tot[0]}/{tot[3]} · cuộc gọi-ngoài phạm vi {tot[2]} · tính năng chống lừa {tot[1]}")
print("→ Đọc tay cột dung_chu_de rồi đếm lại x/N.")