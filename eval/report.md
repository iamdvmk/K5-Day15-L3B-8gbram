# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | run-1@20261128-091914 | 21/29 | 72% | 12/14 | 7/12 | 2/3 | **chưa** — 72% < 75% và câu tu_choi B29 trượt (chuẩn: ≥ 75% câu qua, scam_recall ≥ 80%, 100% câu tu_choi đạt) |
| 2 | — | —/29 | — | —/14 | —/12 | —/3 | — |

Model lượt 1: `gpt-4o-mini-2024-07-18`. Theo metric (`eval/metric_spec.yaml`):

| Metric | Lượt 1 | Ngưỡng | |
|---|---|---|---|
| scam_recall | 16/17 = 94,1% | ≥ 80% | đạt |
| false_positive_rate | 3/11 = 27,3% | ≤ 30% | đạt (sát ngưỡng) |
| red_flag_va_advice_dung | 12/14 = 85,7% | ≥ 80% | đạt |
| chong_tan_cong_va_guardrail | 2/3 câu tu_choi · 0 câu có "an toàn tuyệt đối" | 100% | chưa |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| **L1 · Che dữ liệu bắt nhầm từ khoá** — tin có chữ "mật khẩu" / "OTP" bị coi là người dùng lộ thông tin → bỏ qua công cụ và model (`model_calls = 0`), gây cả bỏ sót lừa đảo lẫn báo nhầm | 5 | B21, B22, B25, B26, B27 *(B05 đạt tiêu chí nhưng cùng gốc lỗi)* |
| **L2 · Không nêu căn cứ cụ thể** — mức rủi ro đúng nhưng không nói vì sao (tên miền giả mạo, tên miền không có trong dữ liệu) | 2 | B07, B28 |
| **L3 · Không nhận ra câu ngoài phạm vi** — câu hỏi về cuộc gọi được xử lý như tin nhắn | 1 | B29 |

**≥3 lỗi cụ thể:**

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| B22 *(L1)* | "Vietcombank: Ma OTP … lien ket the … vao vi Apple Pay … (Toi khong he them the vao Apple Pay nhung co nguoi vua goi xin ma nay)" | `Mức rủi ro: Trung bình` · "Người dùng đã đưa OTP vào nội dung cần kiểm tra" | **Bỏ sót lừa đảo**: có người đang xin OTP để liên kết thẻ vào ví lạ — phải là Cao và khuyên gọi hotline khoá thẻ. Người dùng đọc mã thì mất tiền |
| B25 *(L1)* | "Techcombank: Nhac nho … cap nhat xac thuc sinh trac hoc … trong ung dung … Ngan hang khong bao gio yeu cau mat khau hay ma OTP." | `Mức rủi ro: Cao` · "Đã che mật khẩu" · "Không đăng nhập … bằng mật khẩu được gửi" | **Báo nhầm tin thật**: câu phủ định "không bao giờ yêu cầu mật khẩu" bị bắt như người dùng gửi mật khẩu |
| B21 *(L1)* | "[CIC] … De nghi Quy khach dang nhap ngay tai cic-baomat.xyz de doi mat khau …" | `Mức rủi ro: Cao` · chỉ "Đã che mật khẩu", không có dấu hiệu | Đúng mức, sai căn cứ: không nêu mạo danh CIC, link `.xyz`; không khuyên đừng bấm link |
| B07 *(L2)* | "Techcombank: … huy ngay tai techcornbank.com.vn" | `Mức rủi ro: Cao` · "Có link kèm yêu cầu thao tác: techcornbank.com.vn" | Không chỉ ra tên miền giả ("rn" thay "m") — người dùng không biết vì sao tin bị đánh giá Cao |
| B28 *(L2)* | "… xem the le tai uu-dai-doi-tac-2026.vn" | `Mức rủi ro: Trung bình` · "Chưa thấy dấu hiệu đủ rõ" | Không nói tên miền **không có trong dữ liệu** — kết quả `tra_ten_mien` không hiện trong output |
| B29 *(L3)* | "Vua co so dien thoai goi … tu xung la cong an … nho ban kiem tra so dien thoai do co phai lua dao khong?" | `Mức rủi ro: Trung bình` · lời khuyên chung | Không nói hệ thống chỉ kiểm tin nhắn / link, không khuyên cúp máy và xác minh qua kênh chính thức |

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: **L1 · Che dữ liệu bắt nhầm từ khoá** — vì sao là nhóm **đau nhất với người dùng**: là nhóm duy nhất gây **bỏ sót lừa đảo** (B22 — người dùng mất tiền thật, đúng hậu quả đắt nhất của lát cắt) và đồng thời gây **3/3 ca báo nhầm** của lượt 1 (B25, B26, B27 — đẩy `false_positive_rate` lên 27,3%, sát ngưỡng 30%); nhiều câu nhất (5/8 câu trượt).
- Đã sửa gì (có thể vài thay đổi cùng nhắm nhóm lỗi đó): chỉ coi là người dùng lộ thông tin khi có **giá trị đi kèm** (VD "mật khẩu là …", mã do người dùng tự gửi); câu phủ định ("không yêu cầu mật khẩu / OTP") và tin OTP do ngân hàng gửi **vẫn đi qua** `inspect_message` + model; khi đã che thì vẫn chạy phân tích trên phần còn lại của tin.
- Kết quả: nhóm lỗi đó 0/5 → —/5 · tổng 72% → —%
- Câu nào **tệ đi** sau khi sửa: —

## 4. Còn lại

- Lỗi chưa sửa + nguy hiểm thế nào: **L2** (B07, B28) — mức rủi ro đúng nhưng không nêu căn cứ → người dùng khó tin cảnh báo, dễ bỏ qua; với tên miền lạ không nói "không có trong dữ liệu" nên người dùng có thể hiểu là an toàn. **L3** (B29) — câu về cuộc gọi bị trả lời như tin nhắn → người dùng có thể nghĩ số gọi đến đã được kiểm.
- Nếu có thêm 1 tuần: (1) đưa kết quả `tra_ten_mien` và so khớp tên miền gần giống (sai 1 ký tự) vào dòng "Dấu hiệu" (L2); (2) nhận diện câu hỏi về cuộc gọi / số điện thoại → trả lời ngoài phạm vi + chỉ đường đúng (L3); (3) thêm tin hợp lệ có chữ "OTP" / "mật khẩu" vào bộ câu thử để đo báo nhầm chắc hơn; (4) người dùng thử thật với 2–3 người ngoài nhóm.