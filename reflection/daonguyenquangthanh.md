# Reflection — Đào Nguyễn Quang Thành

1. **Vai trò + phần mình làm:** Mình phụ trách luồng AI kiểm tin nhắn tài chính: nối model thật trong `codebase/ai.py`, xây luồng và guardrail trong `codebase/agent.py`, công cụ che dữ liệu và tra tên miền trong `codebase/tools.py`.
   Mình kiểm các trường hợp link giả, prompt injection, OTP, mật khẩu và yêu cầu ngoài phạm vi; phần code CP3 có trong các commit `fd88214`, `3a6a975`.
   Sau lượt 1, mình sửa nhánh từ chối xác minh cuộc gọi và kiểm thêm các ca tổng hợp; thay đổi sau đó còn ở working tree, chưa tính là commit.

2. **AI hỗ trợ mình thế nào:** Mình dùng Codex (OpenAI) hỗ trợ viết code, prompt trả JSON mức rủi ro/dấu hiệu và gợi ý các ca kiểm guardrail; đã khai ở `docs/ai-usage.md`.
   Mình đọc lại code, đối chiếu output với trace, thử các ca ngoài benchmark và sửa các chỗ AI đề xuất chưa đúng, như bỏ sót URL thứ hai hoặc để chỉ dẫn nguy hiểm lọt vào dòng `Dấu hiệu`.
   Kết quả model chỉ được dùng sau khi lớp quy tắc giữ mức rủi ro tối thiểu và dữ liệu nhạy cảm đã được che.

3. **Một câu thử trượt và bài học:** B29 ở `eval/run-1.csv` hỏi xác minh một số điện thoại gọi đến, nhưng hệ thống lại chấm rủi ro như tin nhắn; câu này làm trượt điều kiện cứng cho nhóm `tu_choi`.
   Mình thêm nhánh từ chối trước model, nói rõ chỉ kiểm văn bản tin nhắn/link và khuyên cúp máy, tự liên hệ cơ quan qua kênh chính thức; đã kiểm cục bộ, còn lượt eval tiếp theo để Vũ chạy và chấm.
   Bài học của mình là guardrail phải kiểm **phạm vi yêu cầu** trước khi chấm nội dung; đồng thời không được để nhánh ngoài phạm vi chạy trước nhánh chặn prompt injection.
