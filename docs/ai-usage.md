# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Codex (OpenAI) | Hỗ trợ viết `codebase/ai.py`, `agent.py`, `tools.py` và test guardrail | Đọc lại luồng, kiểm kết quả mẫu, chạy unit test và `python run.py check` | Thành |
| Prompt / thiết kế lời gọi mô hình | Codex (OpenAI) | Gợi ý system prompt trả JSON mức rủi ro và dấu hiệu, cùng quy tắc chặn sau model | Kiểm các ca link giả, lệnh chèn, OTP/mật khẩu; mức Cao do quy tắc không được model hạ | Thành |
| Đào data (viết script đếm, gợi ý nhãn) | Claude Code (Anthropic) | Viết `evidence/mine_reviews.py` (kéo review, lọc từ khoá, gợi ý nhóm ở cột `nhom_goi_y`, hàm `cat_2_cau` cắt ≤ 2 câu); rà nhãn tay và chỉ ra dòng nghi gán sai; đếm số và soạn nháp `evidence/data-mining.md`, `evidence/summary.md` | Phát đọc tay và gán `loai` / `dung_chu_de` cho cả 566 dòng, tự quyết từng dòng AI chỉ ra; bắt lỗi bản cắt đầu (43 dòng mất từ khoá → cắt lại), lỗi thiếu 1 dòng MoMo (chèn lại), số đếm sai trong nháp; chạy lại script cùng ngày ra đúng 566 / 70.294. Chưa có người thứ hai đọc lại nên chưa đo tỉ lệ khớp nhãn | Phát |
| Data tên miền + DATA_CARD | Claude Code (Anthropic) | Lấy tên miền giả danh từ tinnhiemmang.vn và tên miền chính thức của 11 ngân hàng / ví; soạn nháp `data/DATA_CARD.md` | Phát giới hạn chỉ lấy ngân hàng / ví đã đào review, tự kiểm tay `mbbank.com.vn`, sửa câu chữ trong DATA_CARD; Thành dùng 2 file trong `tra_ten_mien` | Phát |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
