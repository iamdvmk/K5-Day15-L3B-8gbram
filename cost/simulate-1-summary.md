# Tóm tắt mô phỏng simulate-1@20261128-112828

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 15 | 1 | 190 | 42 | 0.7 | 1.1 |
| dung_vua | 24 | 1 | 241 | 53 | 0.9 | 1.3 |
| dung_nhieu | 11 | 2 | 375 | 81 | 1.4 | 2.4 |

Tỉ lệ đạt dùng để tính: 24/29 (83%) — lượt run-2@20261128-104318

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (1.000 người) | Chi phí / tháng — cơ sở (10.000 người) | Chi phí / tháng — cao (100.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.4-nano (vào 0.2 · ra 1.25 $/1M) | $0.00012 (≈ 3 ₫) | $0.00015 (≈ 4 ₫) | $0.00012 (≈ 3 ₫) | $0.5894 (≈ 14.971 ₫) | $5.89 (≈ 149.710 ₫) | $58.94 (≈ 1.497.098 ₫) | $0.00059 (≈ 15 ₫) |
| gpt-5.4-mini (vào 0.75 · ra 4.5 $/1M) | $0.00044 (≈ 11 ₫) | $0.00053 (≈ 14 ₫) | $0.00044 (≈ 11 ₫) | $2.16 (≈ 54.848 ₫) | $21.59 (≈ 548.481 ₫) | $215.94 (≈ 5.484.811 ₫) | $0.0022 (≈ 55 ₫) |
| gpt-5.4 (vào 2.5 · ra 15.0 $/1M) | $0.0015 (≈ 37 ₫) | $0.0018 (≈ 45 ₫) | $0.0015 (≈ 37 ₫) | $7.20 (≈ 182.827 ₫) | $71.98 (≈ 1.828.270 ₫) | $719.79 (≈ 18.282.703 ₫) | $0.0072 (≈ 183 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.2) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-5.4-mini-2026-03-17. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 25.400 ₫ (Tỉ giá tham khảo ~25.400 VND/USD (tự ước tính làm tròn, xem 28/11/2026)).
