# Tóm tắt mô phỏng simulate-1@20261128-115004

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 33 | 1 | 228 | 54 | 0.8 | 1.3 |
| dung_vua | 15 | 2 | 438 | 102 | 1.6 | 2.5 |
| dung_nhieu | 2 | 2 | 385 | 91 | 1.5 | 2.0 |

Tỉ lệ đạt dùng để tính: 24/29 (83%) — lượt run-2@20261128-104318

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (10.000 người) | Chi phí / tháng — cơ sở (50.000 người) | Chi phí / tháng — cao (200.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.4-mini-2026-03-17 (vào 0.75 · ra 4.5 $/1M) | $0.00054 (≈ 14 ₫) | $0.00065 (≈ 16 ₫) | $0.00048 (≈ 12 ₫) | $29.61 (≈ 752.028 ₫) | $148.04 (≈ 3.760.139 ₫) | $592.15 (≈ 15.040.557 ₫) | $0.0030 (≈ 75 ₫) |
| gpt-5.4-nano (vào 0.2 · ra 1.25 $/1M) | $0.00015 (≈ 4 ₫) | $0.00018 (≈ 4 ₫) | $0.00013 (≈ 3 ₫) | $8.09 (≈ 205.426 ₫) | $40.44 (≈ 1.027.130 ₫) | $161.75 (≈ 4.108.521 ₫) | $0.00081 (≈ 21 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.3) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-5.4-mini-2026-03-17. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 25.400 ₫ ((tự ước tính) tỉ giá tham khảo làm tròn · 28/11/2026).
