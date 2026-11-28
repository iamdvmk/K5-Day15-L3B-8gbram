# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Codex (OpenAI) | Hỗ trợ viết `codebase/ai.py`, `agent.py`, `tools.py` và test guardrail | Đọc lại luồng, kiểm kết quả mẫu, chạy unit test và `python run.py check` | Thành |
| Prompt / thiết kế lời gọi mô hình | Codex (OpenAI) | Gợi ý system prompt trả JSON mức rủi ro và dấu hiệu, cùng quy tắc chặn sau model | Kiểm các ca link giả, lệnh chèn, OTP/mật khẩu; mức Cao do quy tắc không được model hạ | Thành |
| Đào data (viết script đếm, gợi ý nhãn) | Claude Code (Anthropic) | Viết `evidence/mine_reviews.py` (kéo review, lọc từ khoá, gợi ý nhóm ở cột `nhom_goi_y`, hàm `cat_2_cau` cắt ≤ 2 câu); rà nhãn tay và chỉ ra dòng nghi gán sai; đếm số và soạn nháp `evidence/data-mining.md`, `evidence/summary.md` | Phát đọc tay và gán `loai` / `dung_chu_de` cho cả 566 dòng, tự quyết từng dòng AI chỉ ra; bắt lỗi bản cắt đầu (43 dòng mất từ khoá → cắt lại), lỗi thiếu 1 dòng MoMo (chèn lại), số đếm sai trong nháp; chạy lại script cùng ngày ra đúng 566 / 70.294. Chưa có người thứ hai đọc lại nên chưa đo tỉ lệ khớp nhãn | Phát |
| Data tên miền + DATA_CARD | Claude Code (Anthropic) | Lấy tên miền giả danh từ tinnhiemmang.vn và tên miền chính thức của 11 ngân hàng / ví; soạn nháp `data/DATA_CARD.md` | Phát giới hạn chỉ lấy ngân hàng / ví đã đào review, tự kiểm tay `mbbank.com.vn`, sửa câu chữ trong DATA_CARD; Thành dùng 2 file trong `tra_ten_mien` | Phát |
| Rà câu hỏi phỏng vấn / khảo sát | Không dùng | Nhóm không làm phỏng vấn / khảo sát; bằng chứng pain chỉ từ review công khai | — | — |
| Viết câu thử (benchmark) | Codex | gợi ý nháp câu thử tu_viet, gợi ý câu tấn công / lệnh chèn | Mỗi câu thử có `source`; Vũ tự chốt `expected` cho cả 29 câu; 13 câu `data_that` dựng lại theo review / cảnh báo chính thức có link, không chép tin nhắn thật của ai | Vũ |
| Sinh data `synthetic` (nếu có) | Không dùng | Không sinh data synthetic bằng script; 16 câu `tu_viet` là câu thử viết tay (xem dòng trên) | — | — |
| Chấm cột `pass` bằng LLM (nếu có) | Không dùng | `scam_recall`, `false_positive_rate` chấm bằng code (đọc dòng "Mức rủi ro:"); 2 metric còn lại chấm tay | Phát chấm độc lập 5 output lượt 2, khớp 5/5 (xem `eval/README.md` mục 3) | Vũ |
| Chi phí (cost) | Claude (Anthropic) | Hướng dẫn chạy `run.py simulate --rate-from eval/run-2.csv`, sửa `cost/personas.yaml`, soạn nháp `cost/cost-estimate.md` | Khánh tự tra giá gpt-5.4-mini / nano trên trang OpenAI (28/11/2026), bỏ giá mẫu trong template; xoá các lần chạy sai model / sai lượt rồi chạy lại; kiểm số khớp `simulate-1-summary.md` | Khánh |
| Giao diện demo `app.py` | Claude (Anthropic) | Viết `app.py` Streamlit gọi lại `answer()` | Khánh chạy thử, sửa lỗi import `codebase/` và lỗi hiện output thừa; không đổi logic đánh giá | Khánh |
| Slide, văn bản | Claude (Anthropic) | Dựng nháp `demo-slides.pdf`, kịch bản 5 phút; `eval/report.md`, canvas | Khánh kiểm mọi số trên slide với file trong repo; bỏ số lượt 1 chưa xác nhận khỏi slide | Khánh |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).