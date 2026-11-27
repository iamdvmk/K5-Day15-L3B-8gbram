# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Review Google Play về lừa đảo của app ngân hàng / ví (`evidence/reviews_matched.csv`)

| | |
|---|---|
| Dùng để làm gì | **Đào bằng chứng pain** (`evidence/data-mining.md`) · gốc kịch bản cho 3 câu thử `data_that` B16–B18 (Dataset 3) |
| Từ đâu | Review công khai trên Google Play của 11 app: MoMo, Vietcombank, MB Bank, Techcombank, BIDV, VietinBank, ZaloPay, TPBank, Viettel Money, VNPAY, Cake (`lang=vi`, `country=vn`), kéo bằng `google-play-scraper`. Link từng app ở cột `link_nguon` |
| Xử lý những bước gì | **Kéo:** mỗi app 5.000 mới nhất + 5.000 "liên quan nhất", bỏ trùng theo `reviewId` → 70.294 review · **Lọc:** giữ review khớp từ khoá ngữ cảnh lừa đảo → 566 review · **Ẩn danh:** bỏ tên, ảnh đại diện, `reviewId`; **mỗi review chỉ giữ tối đa 2 câu** (luật dùng dữ liệu mục 5) · **Gán nhãn tay:** `loai` (7 nhóm, định nghĩa ở `evidence/data-mining.md`) + `dung_chu_de` (1 = người viết / người thân đã bị lừa hoặc bị chiếm TK) · Script: `evidence/mine_reviews.py` |
| Số dòng / số đoạn | **N = 566 review đã đọc và gắn nhãn** (lọc từ 70.294 review đã kéo) · **22/566 (3,9%) `dung_chu_de = 1`**, trong đó 2 dòng đúng lát cắt tin nhắn / link giả danh |
| Phiên bản / ngày lấy | Ngày xem 27/11/2026 · review có ngày từ 30/08/2023 đến 26/11/2026 · `google-play-scraper` 1.2.7 |
| Nhãn | **thật** (review công khai, đã ẩn danh) · nhãn do 1 thành viên đọc tay, có AI hỗ trợ rà lại (`docs/ai-usage.md`) |
| Giới hạn | Review dùng để chấm app nên phần lớn là phàn nàn lỗi / phí → chỉ cho **cận dưới**, không đo được tần suất nhận tin giả · lệch về 1★ · bộ lọc từ khoá bỏ sót review không dùng từ trong danh sách · 1 người gán nhãn, chưa kiểm độ thống nhất · mẫu "liên quan nhất" do Google Play chọn, không ngẫu nhiên · chạy lại ngày khác ra mẫu số hơi khác · **chỉ 2/22 dòng nói đúng kênh tin nhắn/link → cần nguồn thứ hai kiểm lại** |

## Dataset 2 · Câu thử tự dựng (`eval/benchmark.csv`, B01–B15, `source = tu_viet`)

| | |
|---|---|
| Dùng để làm gì | Bộ câu thử: tin lừa đảo dựng lại (B01–B04, B07, B12–B14), tin ngân hàng hợp lệ dựng mẫu (B05, B06, B08, B11, B15), câu tấn công / từ chối (B09, B10) |
| Từ đâu | Nhóm viết tay theo kịch bản trong cảnh báo công khai của ngân hàng / VNCERT / công an (brandname giả, khoá tài khoản, điểm thưởng, phạt nguội, xin OTP, link sai 1 ký tự, rút gọn link, APK) và định dạng tin OTP / biến động số dư / thông báo bảo trì công khai. **Không dùng tin nhắn thật của người thật** (luật dùng dữ liệu mục 6) |
| Xử lý những bước gì | Mọi link là tên miền giả (`.top`, `.cc`, `.info`, `.vip`, sai 1 ký tự) · STK `x...x123`, số dư `x,xxx,xxx`, OTP là số ngẫu nhiên · không có tên người |
| Số dòng / số đoạn | 15 câu · thuong 7 · kho 6 · tu_choi 2 |
| Phiên bản / ngày lấy | v1 27/11/2026 |
| Nhãn | **`synthetic`** · cách sinh: viết tay [*có / không* — Vũ điền] dùng LLM gợi ý biến thể câu chữ (nếu có: prompt ở `docs/ai-usage.md`) · seed: không áp dụng · người kiểm: [*Khánh*] · đã kiểm tay **15/15** |
| Giới hạn | Tin dựng "sạch" hơn tin thật (ít teencode, ít lỗi chính tả) · cả bộ chỉ 6 tin hợp lệ (B05, B06, B08, B11, B15, B23) → `false_positive_rate` đổi theo bước ~17% · chưa phủ QR, ảnh chụp, cuộc gọi |

## Dataset 3 · Câu thử từ kịch bản thật (`eval/benchmark.csv`, B16–B23, `source = data_that`)

| | |
|---|---|
| Dùng để làm gì | Câu thử bám lừa đảo có thật (8/23 = 35% bộ câu thử, đạt yêu cầu ≥1/3 của R4) |
| Từ đâu | **B16–B18:** viết lại theo kịch bản người dùng kể trong review ở Dataset 1 (hoá đơn điện giả, "mở nhầm tài khoản tín dụng ảo", dùng CCCD vay hộ) — cột `source` cần ghi app · số sao · ngày của review gốc [*Vũ kiểm*] · **B19–B23:** theo tin mẫu trong bài cảnh báo công khai của Vietcombank / CIC [*Vũ điền link + ngày xem từng câu*] |
| Xử lý những bước gì | B16–B18 viết lại thành dạng tin nhắn, không chép nguyên văn review · B19–B23 giữ nội dung tin mẫu, link đã làm vô hại / thay tên miền giả, bỏ SĐT · STK dạng `x...x889` |
| Số dòng / số đoạn | 8 câu · thuong 4 · kho 4 |
| Phiên bản / ngày lấy | Ngày xem 27/11/2026 |
| Nhãn | **thật** về kịch bản (review / cảnh báo có thật), câu chữ đã viết lại — ghi rõ ở cột `source` |
| Giới hạn | Chỉ gồm lừa đảo đã bị phát hiện và cảnh báo → thiếu biến thể mới · B16–B18 là diễn giải của nhóm từ lời kể, có thể lệch tin gốc |

## Dataset 4 · Dữ liệu công cụ của bản chạy thử *(bổ sung ở CP3)*

*Chờ Thành: `codebase/tools.py` đọc dữ liệu gì trong `data/` — dự kiến `data/ten_mien_lua_dao.csv` (tên miền bị báo cáo trên tinnhiemmang.vn, đã làm vô hại `[.]`, ghi ngày xem) và `data/ten_mien_ngan_hang.csv` (tên miền chính thức của ngân hàng). Mỗi file một mục theo bảng trên.*