# Canvas — [tên nhóm] · Track [A–F]

> Điền ở guide bước 1.4. CP1 17:00 Thứ Sáu 27/11: nộp bản đầu, đủ 7 dòng (dòng 4 được ghi giả thuyết + nguồn sẽ kiểm).
> CP2 19:30 Thứ Sáu 27/11: cập nhật (số bằng chứng đầu, lát cắt đã chốt) và điền dòng "Đã đổi gì so với CP1".
> Track F: chép thêm thẻ đề của nhóm (khung trong file track F) xuống dưới bảng này.

| # | Dòng | Nhóm điền |
|---|---|---|
| 1 | Track + lát cắt dự kiến | **Track E · Tài chính cá nhân** — kiểm tra tin nhắn nghi giả danh ngân hàng trước khi người dùng bấm link / làm theo |
| 2 | Người dùng chính (một vai cụ thể — không phải "học viên nói chung") | Khách hàng cá nhân dùng app ngân hàng/ví (Vietcombank, MB Bank, MoMo) **ngay lúc vừa nhận một tin nhắn mang danh ngân hàng có link hoặc yêu cầu thao tác** và đang phân vân có làm theo không |
| 3 | Pain một câu: ai — đang làm gì — vướng đâu — hậu quả | Khách hàng app ngân hàng — vừa nhận tin nhắn mang danh ngân hàng chứa link/yêu cầu OTP — không phân biệt được thật/giả vì tin giả nằm chung luồng với tin thật và link chỉ sai vài ký tự — bấm link, nhập OTP và mất tiền trong tài khoản |
| 4 | Bằng chứng đầu — CP1: giả thuyết + nguồn sẽ kiểm · CP2: số đầu tiên + 1 trích dẫn | **Giả thuyết:** một phần đáng kể review app ngân hàng/ví kể việc nhận tin giả mạo hoặc bị lừa mất tiền. **Nguồn kiểm:** đào 2.000 review mới nhất/app trên Google Play (MoMo, Vietcombank, MB Bank) bằng script `evidence/mine_reviews.py`. **Kết quả sơ bộ:** 315/6.000 review khớp từ khoá (chưa đọc tay) — CP2 sẽ cập nhật số đã đọc tay + 1 trích dẫn |
| 5 | **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả) | Khách hàng app ngân hàng **dán một tin nhắn đáng ngờ** → AI **chấm mức rủi ro (Cao/TB/Thấp), chỉ ra dấu hiệu và khuyên bước tiếp theo** → đo được **tỉ lệ bắt đúng tin lừa đảo** và **tỉ lệ báo nhầm tin thật** |
| 6 | AI tự làm đến đâu + 1 dòng lý do: sai thì ai chịu gì | AI **chỉ cảnh báo**, không chặn tin, không tự thao tác; không bao giờ nói "an toàn tuyệt đối", không chắc thì khuyên gọi hotline in trên thẻ. **Lý do:** bỏ sót tin lừa đảo thì người dùng mất tiền thật; báo nhầm chỉ tốn một cuộc gọi kiểm tra → ưu tiên không bỏ sót |
| 7 | Phân công có tên | **Khánh** (ĐT): spec, guardrail, slide & thuyết trình · **Thành**: dựng luồng AI — run.py, prompt, gọi model, video · **Phát**: bằng chứng — đào review, evidence, DATA_CARD · **Vũ**: eval & chi phí — benchmark, metric, eval 2 lượt, simulate |
| — | *(CP2)* Đã đổi gì so với CP1 | |
