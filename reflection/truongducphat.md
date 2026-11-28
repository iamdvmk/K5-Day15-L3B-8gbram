# Reflection — Trương Đức Phát

> Làm ở guide bước 5.3. Hạn: **23:59 Thứ Bảy 28/11**.

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   Phụ trách bằng chứng pain và data của nhóm 8gbram (Track E). Viết `evidence/mine_reviews.py` kéo 70.294 review Google Play của 11 app ngân hàng / ví, lọc ra 566 review rồi đọc tay gán `loai` / `dung_chu_de` trong `evidence/reviews_matched.csv`, viết `evidence/data-mining.md` (commit `4603d6d`). Sang CP3, cắt mỗi review còn ≤ 2 câu kèm link nguồn và viết `evidence/summary.md` với 7 trích dẫn (`114deed`); lập 2 file tên miền `data/ten_mien_lua_dao.csv` (27 tên miền, nguồn tinnhiemmang.vn) và `data/ten_mien_ngan_hang.csv` (11 tên miền chính thức) cho công cụ `tra_ten_mien` của Thành (`be39db0`, `5c41fa9`); viết `data/DATA_CARD.md` Dataset 1–5 (`2180b35`, `e559089`) và ghi changelog / khai AI phần mình (`ba8800c`).
   Kết quả chính: chỉ 22/566 review kể bị lừa / bị chiếm tài khoản, 2/22 đúng kênh tin nhắn / link → giả thuyết ban đầu "nhiều review kể bị lừa" không đúng, review chỉ cho cận dưới.

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   Dùng Claude Code để viết script đào review, hàm cắt 2 câu, đếm số, soạn nháp data-mining / summary / DATA_CARD và lấy danh sách tên miền (khai ở `docs/ai-usage.md`). Phần nhãn mình tự đọc và quyết cả 566 dòng; các ca lưng chừng (tự gia hạn, tự trừ tiền, thưởng giới thiệu không về, ưu đãi nạp thẻ) mình chốt là 0 vì đó là chửi app chứ không phải bị lừa.
   Chỗ phải sửa output AI: (a) bản cắt 2 câu đầu tiên lấy 2 câu đầu nên 43 dòng mất luôn từ khoá đã khớp → bắt cắt lại, ưu tiên câu chứa từ khoá; (b) file sau khi gán nhãn bị thiếu 1 dòng MoMo, phải chạy lại script để tìm và chèn lại, rồi cập nhật số dòng các ví dụ; (c) nháp DATA_CARD đếm sai số câu thử của Vietcombank (ghi 6/13, đúng là 4/13); (d) AI lấy tên miền lừa đảo của cả những ngân hàng nhóm không đào → mình giới hạn chỉ 11 app đã cào, và tự kiểm tay `mbbank.com.vn`.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   B21: tin giả CIC đòi "dang nhap ngay tai cic-baomat.xyz de doi mat khau". Cả lượt 1 và lượt 2 đều trượt: guardrail thấy chữ "doi mat khau" liền coi là người dùng gửi mật khẩu và dừng trước, nên `tool_calls = 0` — công cụ `tra_ten_mien` dùng data tên miền của mình **không hề được gọi**, output không nhắc gì tới link `.xyz`. Mà kể cả có gọi, `cic-baomat.xyz` cũng không nằm trong danh sách, vì mình chỉ lấy tên miền giả danh ngân hàng / ví và danh sách chỉ biết tên miền **đã** bị báo cáo.
   Bài học: data đúng chưa đủ, phải kiểm xem luồng có thật sự chạm tới data không (đọc cột `tool_calls` trong trace); và danh sách tên miền tĩnh chỉ là một tín hiệu, không có trong danh sách phải ra "chưa xác định", còn dấu hiệu khác (đuôi lạ, đòi đăng nhập qua link) phải tự đứng được.
