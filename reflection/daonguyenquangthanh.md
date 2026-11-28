# Reflection — Đào Nguyễn Quang Thành

1. **Vai trò + phần mình làm:** Ở CP2, mình dựng luồng mock trong `codebase/agent.py` và `codebase/tools.py` để chạy thử từ đầu vào đến kết quả; hai commit là `a7b9b86` và `9211a3f`.
   Sang CP3, mình nối model thật trong `codebase/ai.py`, xây guardrail và tra tên miền trong `agent.py`, `tools.py`; các commit chính là `fd88214` và `3a6a975`.
   Sau lượt 1, mình sửa từ chối xác minh cuộc gọi, kiểm prompt injection, che dữ liệu và nhiều URL; phần cải tiến cùng reflection được push ở commit `dc8d90f`.

2. **AI hỗ trợ mình thế nào:** Codex hỗ trợ mình dựng luồng mock CP2, prompt trả JSON mức rủi ro/dấu hiệu và gợi ý guardrail ngoài benchmark; đã khai ở `docs/ai-usage.md`.
   Mình đọc lại code, đối chiếu output với trace, thử các ca ngoài benchmark và sửa các chỗ AI đề xuất chưa đúng, như bỏ sót URL thứ hai hoặc để chỉ dẫn nguy hiểm lọt vào dòng `Dấu hiệu`.

3. **Một câu thử trượt và bài học:** B29 ở `eval/run-1.csv` hỏi xác minh một số điện thoại gọi đến, nhưng hệ thống lại chấm rủi ro như tin nhắn; câu này làm trượt điều kiện cứng cho nhóm `tu_choi`.
   Mình thêm nhánh từ chối trước model, nói rõ chỉ kiểm văn bản tin nhắn/link và khuyên cúp máy, tự liên hệ cơ quan qua kênh chính thức; đã kiểm cục bộ.
   Bài học: guardrail phải kiểm **phạm vi yêu cầu** trước khi chấm nội dung; đồng thời không được để nhánh ngoài phạm vi chạy trước nhánh chặn prompt injection.
