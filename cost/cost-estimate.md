# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí**.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu — `dung_it` 60% · 2 phiên / người / tháng · 1 lượt hỏi / phiên · `dung_vua` 30% · 6 phiên · 2 lượt · `dung_nhieu` 10% · 15 phiên · 2 lượt (hỏi cả câu `thuong`, `kho`, `tu_choi`). Trung bình **4,5 phiên / người / tháng**. Nguồn: *(tự ước tính)* — nhóm không phỏng vấn / khảo sát; review trong `evidence/` không đo được tần suất.
- **Số người dùng thật** 3 kịch bản: thấp **10.000** · cơ sở **50.000** · cao **200.000**. Nguồn: *(tự ước tính)* — người dùng tính năng kiểm tin nhắn trong 1 app ngân hàng / ví tầm trung tại VN (thấp = thí điểm, cơ sở = một phần nhỏ khách hàng số, cao = mở rộng toàn app).
- **Giá** 2 mức model (USD / 1 triệu token, giá Standard): **gpt-5.4-mini** vào 0,75 · ra 4,50 — [developers.openai.com/api/docs/models/gpt-5.4-mini](https://developers.openai.com/api/docs/models/gpt-5.4-mini), xem 28/11/2026 · **gpt-5.4-nano** vào 0,20 · ra 1,25 — [developers.openai.com/docs/models/gpt-5.4-nano](https://developers.openai.com/docs/models/gpt-5.4-nano), xem 28/11/2026
- **Tỉ lệ đạt** dùng để tính: **24/29 (83%)** — lượt `run-2@20261128-104318` (lượt 2)
- Đo token trên model **gpt-5.4-mini-2026-03-17**, tính giá model **gpt-5.4-mini** và **gpt-5.4-nano**. Dòng nano chỉ để so sánh: dùng cùng số token đo trên mini và **giả định cùng tỉ lệ đạt 83%** — chưa chạy lượt nào trên nano.
- Tỉ giá: 1 USD = 25.400 ₫ *(tự ước tính, 28/11/2026)*.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · tóm tắt `cost/simulate-1-summary.md` · trace `traces/simulate-1.jsonl` · **50 phiên** · seed **42** · chạy thật qua bản chạy thử, token đọc từ log · phiên lỗi 0/50

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 33 | 1 | 228 | 54 | 0.8 | 1.3 |
| dung_vua | 15 | 2 | 438 | 102 | 1.6 | 2.5 |
| dung_nhieu | 2 | 2 | 385 | 91 | 1.5 | 2.0 |

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp (10.000 người) | / tháng — cơ sở (50.000 người) | / tháng — cao (200.000 người) | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|
| **gpt-5.4-mini-2026-03-17** (đã đo) | $0.00054 (≈ 14 ₫) | **$0.00065 (≈ 16 ₫)** | $29.61 (≈ 752.028 ₫) | **$148.04 (≈ 3.760.139 ₫)** | $592.15 (≈ 15.040.557 ₫) | **$0.0030 (≈ 75 ₫)** |
| gpt-5.4-nano (so sánh, giả định 83%) | $0.00015 (≈ 4 ₫) | $0.00018 (≈ 4 ₫) | $8.09 (≈ 205.426 ₫) | $40.44 (≈ 1.027.130 ₫) | $161.75 (≈ 4.108.521 ₫) | $0.00081 (≈ 21 ₫) |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%**. Chi phí / câu hỏi đạt (mini): $0.00048 (≈ 12 ₫).

**Ghi chú đọc số:**
- 7/50 phiên có 0 token: câu bị lớp quy tắc chặn trước model (lệnh chèn, mật khẩu / OTP) — vẫn tính vào trung bình.
- Mẫu ngẫu nhiên seed 42 chỉ ra 2 phiên `dung_nhieu` (tỉ lệ khai báo 10% → kỳ vọng ~5) → token / phiên của kiểu này kém tin cậy; ảnh hưởng nhỏ vì chi phí tháng tính theo tỉ lệ và tần suất khai báo trong `personas.yaml`.

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): **4,5 lần kiểm × 5 phút ≈ 22,5 phút** tự kiểm / gọi hotline được rút ngắn *(5 phút / lần: tự ước tính)*; quy ra tiền ở mức 30.000 ₫ / giờ *(tự ước tính)* ≈ **11.000 ₫ / người / tháng** — chưa tính phần lớn nhất là tiền tránh bị lừa (review: có ca mất hơn 500 triệu).
- Chi phí / người / tháng (cơ sở, model gpt-5.4-mini): **≈ 75 ₫ ($0.0030)**
- **Kết luận một dòng — đáng làm không:** **Đáng làm** — chi phí model ≈ 75 ₫ / người / tháng, nhỏ hơn hơn 100 lần giá trị thời gian tiết kiệm (≈ 11.000 ₫) và không đáng kể so với một lần bị lừa; kể cả kịch bản cao 200.000 người chỉ ≈ 15 triệu ₫ / tháng. Rủi ro chính không nằm ở chi phí mà ở chất lượng (bỏ sót B22, báo nhầm 30%).

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Đổi sang gpt-5.4-nano giảm chi phí ~3,7 lần (75 ₫ → 21 ₫ / người / tháng) nhưng **chưa đo tỉ lệ đạt** trên nano — phải chạy lại bộ 29 câu trước khi đổi.
- Chi phí ngoài model (hosting, duy trì danh sách tên miền lừa đảo, người cập nhật quy tắc) chưa tính.