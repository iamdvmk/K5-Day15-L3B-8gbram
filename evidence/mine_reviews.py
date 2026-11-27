"""Đào review Google Play về lừa đảo / tin nhắn giả mạo — bằng chứng pain Track E.

Cài:   pip install google-play-scraper pandas
Chạy:  python evidence/mine_reviews.py
Ra:    evidence/reviews_matched.csv (review khớp từ khoá, đã bỏ tên người viết)
       + in ra x/N theo từng app để chép vào evidence/summary.md
"""
import re
import pandas as pd
from google_play_scraper import reviews, Sort

# Kiểm lại ID trên link Play Store (phần ?id=...) trước khi chạy
APPS = {
    "MoMo": "com.mservice.momotransfer",
    "Vietcombank": "com.VCB",
    "MB Bank": "com.mbmobile",
    # thêm app khác: "Tên": "package.id",
}
N_PER_APP = 2000  # số review mới nhất kéo về mỗi app

KEYWORDS = re.compile(
    r"lừa đảo|bị lừa|mạo danh|giả mạo|tin nhắn giả|sms giả|link lạ|đường link"
    r"|chiếm đoạt|mất tiền|bị trừ tiền|hack|scam|otp",
    re.IGNORECASE,
)

rows, summary = [], []
for app, app_id in APPS.items():
    data, _ = reviews(app_id, lang="vi", country="vn", sort=Sort.NEWEST, count=N_PER_APP)
    hits = [r for r in data if r["content"] and KEYWORDS.search(r["content"])]
    summary.append((app, len(hits), len(data)))
    for r in hits:
        rows.append({
            "app": app,
            "sao": r["score"],
            "ngay": r["at"].date().isoformat(),
            "noi_dung": r["content"].replace("\n", " "),
            "khop": ", ".join(sorted({m.lower() for m in KEYWORDS.findall(r["content"])})),
            "dung_chu_de": "",  # đọc tay: 1 = đúng là pain lừa đảo/tin giả, 0 = khớp nhầm
        })

pd.DataFrame(rows).to_csv("evidence/reviews_matched.csv", index=False, encoding="utf-8-sig")
print(f"Lọc theo từ khoá, {N_PER_APP} review mới nhất / app, lang=vi, country=vn")
for app, x, n in summary:
    print(f"  {app}: {x}/{n} review khớp ({x / max(n, 1):.1%})")
print("→ Mở reviews_matched.csv, điền cột dung_chu_de, đếm lại x/N sau khi đọc tay.")