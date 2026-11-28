# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate --rate-from eval/run-2.csv` → chép bảng từ `cost/simulate-1-summary.md`.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** - đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu người dùng app ngân hàng / ví điện tử (khớp `spec.md` §2, trung bình ~4,15 tin/người/tháng):
  - `dung_it`: 35% · 1 phiên/người/tháng · 1 lượt hỏi/phiên
  - `dung_vua`: 45% · 4 phiên/người/tháng · 1 lượt hỏi/phiên
  - `dung_nhieu`: 20% · 10 phiên/người/tháng · 2 lượt hỏi/phiên *(gồm cả `tu_choi`)*
  - Nguồn: `spec.md` §2 *(tự ước tính - `evidence/summary.md` không dùng phỏng vấn/khảo sát)*.
- **Số người dùng thật** 3 kịch bản: thấp **1.000** (nhóm thí điểm, khớp `spec.md` §2) · cơ sở **10.000** (1 phân khúc khách hàng thường xuyên) · cao **100.000** (mở rộng đại trà trên 1 app ngân hàng/ví tầm trung). Nguồn: `spec.md` §2 & `cost/personas.yaml` *(tự ước tính)*.
- **Giá** 3 mức model (`https://openai.com/api/pricing` · xem 28/11/2026, USD / 1M token):
  - `gpt-5.4-nano` (rẻ hơn): vào `$0.20` · ra `$1.25`
  - `gpt-5.4-mini` (đang chạy thật): vào `$0.75` · ra `$4.50`
  - `gpt-5.4` (mạnh hơn): vào `$2.50` · ra `$15.00`
  - Tỉ giá quy đổi: `1 USD = 25.400 ₫` *(tự ước tính làm tròn, xem 28/11/2026)*.
- **Tỉ lệ đạt** dùng để tính: **24/29 (83%)** - lượt `run-2@20261128-104318` (`eval/run-2.csv`).
- **Lưu ý đo token:** Đo token thật trên model **`gpt-5.4-mini-2026-03-17`**, tính giá cho cả `gpt-5.4-nano`, `gpt-5.4-mini` và `gpt-5.4` *(model khác bộ tách token có thể lệch nhẹ số token thực tế)*.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID `simulate-1@20261128-112828` · **50 phiên** · seed `42` · **0/50 phiên lỗi** · trace: `traces/simulate-1.jsonl`.

**Thống kê token & lượt gọi theo persona (chép từ `cost/simulate-1-summary.md`):**

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| `dung_it` | 15 | 1 | 190 | 42 | 0.7 | 1.1 |
| `dung_vua` | 24 | 1 | 241 | 53 | 0.9 | 1.3 |
| `dung_nhieu` | 11 | 2 | 375 | 81 | 1.4 | 2.4 |

**Bảng chi phí theo 3 mức model và 3 kịch bản quy mô (chép từ `cost/simulate-1-summary.md`):**

| Model (giá $/1M token) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | / tháng - thấp (1.000 người) | / tháng - cơ sở (10.000 người) | / tháng - cao (100.000 người) | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| `gpt-5.4-nano` (0.20 / 1.25) | $0.00012 (≈ 3 ₫) | $0.00015 (≈ 4 ₫) | $0.00012 (≈ 3 ₫) | $0.5894 (≈ 14.971 ₫) | $5.89 (≈ 149.710 ₫) | $58.94 (≈ 1.497.098 ₫) | $0.00059 (≈ 15 ₫) |
| **`gpt-5.4-mini` (0.75 / 4.50)** *(đang dùng)* | **$0.00044 (≈ 11 ₫)** | **$0.00053 (≈ 14 ₫)** | **$0.00044 (≈ 11 ₫)** | **$2.16 (≈ 54.848 ₫)** | **$21.59 (≈ 548.481 ₫)** | **$215.94 (≈ 5.484.811 ₫)** | **$0.0022 (≈ 55 ₫)** |
| `gpt-5.4` (2.50 / 15.00) | $0.0015 (≈ 37 ₫) | $0.0018 (≈ 45 ₫) | $0.0015 (≈ 37 ₫) | $7.20 (≈ 182.827 ₫) | $71.98 (≈ 1.828.270 ₫) | $719.79 (≈ 18.282.703 ₫) | $0.0072 (≈ 183 ₫) |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt (`83%`) - **không coi như đạt 100%**. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (`1.2`) ÷ tỉ lệ đạt.

## 3. So với impact

- **Impact / người / tháng (`spec.md` §2):** tiết kiệm trung bình **~20 phút/người/tháng** (4 tin × 5 phút tự kiểm tra / gọi hotline, *(tự ước tính)* → ~333 giờ/tháng ở quy mô thí điểm 1.000 người), và quan trọng nhất là **giảm nguy cơ mất tiền thật** (review trong `evidence/summary.md`: có nạn nhân mất hơn 500 triệu chỉ vì bấm 1 link lạ, hoặc bị vay 40 triệu).
- **Chi phí / người / tháng (cơ sở, model `gpt-5.4-mini`):** **$0.0022 (≈ 55 ₫/người/tháng)** - tương đương **≈ 54.848 ₫/tháng** cho cả nhóm thí điểm 1.000 người và **≈ 548.481 ₫/tháng** ở mức cơ sở 10.000 người.
- **Kết luận một dòng - đáng làm không:** **Rất đáng làm về mặt chi phí** - chi phí API chỉ ~55 ₫/người/tháng (chỉ cần giúp ngăn chặn 1 vụ lừa 5 triệu đồng đã đủ bù ~9 tháng chi phí API cho 10.000 người dùng), nhưng cần tiếp tục sửa 5 câu lỗi guardrail/phủ định còn lại trước khi triển khai rộng.

## 4. Độ nhạy & chi phí ngoài model *(tham khảo thêm)*

- **Độ nhạy theo model:** Chuyển xuống `gpt-5.4-nano` giảm chi phí ~3,7× (còn ~15 ₫/người/tháng) nhưng cần chạy lại bộ 29 câu thử để chắc chắn không tụt `scam_recall` dưới 80%. Ngoài ra, lớp quy tắc/guardrail trước LLM đã chặn sớm một phần phiên (`0.7–1.4` lần gọi model/phiên) giúp tiết kiệm token tự nhiên.
- **Chi phí ngoài model (chưa tính trong bảng trên):** hosting backend nhỏ + cập nhật định kỳ danh sách tên miền lừa đảo (`tinnhiemmang.vn` / `chongluadao.vn`) và giám sát log cảnh báo sai.
