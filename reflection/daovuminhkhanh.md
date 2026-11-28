# Reflection — Đào Vũ Minh Khánh

> Làm ở guide bước 5.3. Hạn: **23:59 Thứ Bảy 28/11**.

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   Đội trưởng nhóm 8gbram (L3B, Track E): nộp form cả 4 checkpoint, điều phối chia việc và gộp nhánh. Viết `canvas.md`, `TEAMS.md` (CP1–CP2) và phần lớn `spec.md`: §0–§3, §5–§6 (commit `c6e7e1b`), §8–§9, sửa §0/§4/§7 và changelog §10 (commit `8503cc2`). Ở CP4 tiếp quản phần mô phỏng chi phí: sửa `cost/personas.yaml` (giá gpt-5.4-mini / nano, quy mô 10.000 / 50.000 / 200.000), chạy `python run.py simulate --rate-from eval/run-2.csv` ra `cost/simulate-1.csv`, viết `cost/cost-estimate.md` (chi phí / task thành công ≈ 16 ₫). Thêm giao diện demo `app.py` (Streamlit gọi lại `answer()`).

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   Dùng Claude (chat) để soạn nháp spec / canvas / metric. Những chỗ phải tự kiểm và sửa: (a) số liệu AI gợi ý ban đầu (30/565) lệch với bộ nhãn đọc tay của Phát (22/566), và 64 hay 65 review chặn nhầm — mình phải đếm lại trực tiếp trong `evidence/reviews_matched.csv` rồi mới chốt 65 theo cột `loai`; (b) bản nháp §2 dùng persona 1 / 4 / 10 tin, không khớp `personas.yaml` → phải đồng bộ lại; (c) AI đề xuất điểm cho lượt chạy thử bằng gpt-4o-mini của mình, nhưng nhóm giữ lượt 1 của Vũ (gpt-5.4-mini) làm chính thức nên bỏ bản đó; giá gpt-5.4-mini có link.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   B22: tin OTP thật của Vietcombank để liên kết thẻ vào Apple Pay, kèm câu "có người vừa gọi xin mã này" — đúng kịch bản người dùng sắp mất thẻ. Cả lượt 1 và lượt 2 đều chỉ ra "Trung bình", vì lớp che dữ liệu thấy chữ "OTP" liền coi là người dùng tự lộ mã và dừng trước khi gọi công cụ và model. Bài học: lớp an toàn đặt trước model cũng là code có thể sai, và có thể sai theo hướng nguy hiểm nhất (bỏ sót lừa đảo) — nên phải có câu thử nhắm thẳng vào chính lớp chặn, và khi quy tắc kích hoạt thì vẫn phải cho phần còn lại của tin đi qua phân tích, thay vì dừng hẳn. Lượt 2 nhóm ưu tiên sửa B29 vì là điều kiện cứng của chuẩn "đạt", nên lỗi này vẫn còn và được ghi ở `eval/report.md` mục 4.