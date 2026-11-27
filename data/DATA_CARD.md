# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Review Google Play về lừa đảo của app ngân hàng / ví (`evidence/reviews_matched.csv`)

| | |
|---|---|
| Dùng để làm gì | **Đào bằng chứng pain** (`evidence/data-mining.md`) · gốc kịch bản cho 3 câu thử `data_that` B16–B18 (Dataset 3) |
| Từ đâu | Review công khai trên Google Play của 11 app: MoMo, Vietcombank, MB Bank, Techcombank, BIDV, VietinBank, ZaloPay, TPBank, Viettel Money, VNPAY, Cake (`lang=vi`, `country=vn`), kéo bằng `google-play-scraper`. Link từng app ở cột `link_nguon` |
| Xử lý những bước gì | **Kéo:** mỗi app 5.000 mới nhất + 5.000 "liên quan nhất", bỏ trùng theo `reviewId` → 70.294 review · **Lọc:** giữ review khớp từ khoá ngữ cảnh lừa đảo → 566 review · **Ẩn danh:** bỏ tên, ảnh đại diện, `reviewId` · **Gán nhãn tay** (trên nguyên văn): `loai` (7 nhóm, định nghĩa ở `evidence/data-mining.md`) + `dung_chu_de` (1 = người viết / người thân đã bị lừa hoặc bị chiếm TK) · **Cắt sau khi gán nhãn: mỗi review giữ tối đa 2 câu** (luật dùng dữ liệu mục 5), phần bỏ đánh dấu `[…]`: 6 dòng `dung_chu_de = 1` chọn tay 2 câu chứa ý bị lừa, các dòng còn lại giữ câu chứa từ khoá đã khớp + 1 câu liền kề → 117/566 dòng bị cắt, nhãn không đổi · Thêm cột `link_nguon` (trang app trên Google Play) + `ngay_xem` · Script: `evidence/mine_reviews.py` (v3: tự cắt 2 câu, không ghi đè file đã gán nhãn) |
| Số dòng / số đoạn | **N = 566 review đã đọc và gắn nhãn** (lọc từ 70.294 review đã kéo) · **22/566 (3,9%) `dung_chu_de = 1`** (= 22/70.294, 0,03% trên toàn bộ review), trong đó 2 dòng đúng lát cắt tin nhắn / link giả danh |
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
| Nhãn | **`synthetic`** · cách sinh: nhóm chọn kịch bản và nhãn, LLM gợi ý biến thể câu chữ (prompt + model ghi ở `docs/ai-usage.md`) · seed: không áp dụng (sinh tương tác, đã chỉnh tay từng câu) · người kiểm: Khánh · đã kiểm tay **15/15** |
| Giới hạn | Tin dựng "sạch" hơn tin thật (ít teencode, ít lỗi chính tả) · cả bộ chỉ 6 tin hợp lệ (B05, B06, B08, B11, B15, B23) → `false_positive_rate` đổi theo bước ~17% · chưa phủ QR, ảnh chụp, cuộc gọi |

## Dataset 3 · Câu thử từ kịch bản thật (`eval/benchmark.csv`, B16–B23, `source = data_that`)

| | |
|---|---|
| Dùng để làm gì | Câu thử bám lừa đảo có thật (8/23 = 35% bộ câu thử, đạt yêu cầu ≥1/3 của R4) |
| Từ đâu | **B16–B18:** viết lại theo kịch bản người dùng kể trong review ở Dataset 1 — B16: TPBank 1★ 17/01/2025, dòng 341 (giả thu tiền điện nước) · B17: Cake 1★ 05/01/2025, dòng 519 (lừa mở "tk tín dụng ảo" để xoá) · B18: MoMo 5★ 27/09/2026, dòng 45 + Viettel Money 1★ 11/05/2026, dòng 397 (lừa vay tiền hộ) — số dòng trong `evidence/reviews_matched.csv` · **B19, B20, B22:** cảnh báo chính thức trên vietcombank.com.vn (tên miền giả `vieetcom.top`, `diem-vietcom-priority.com`; thủ đoạn xin OTP liên kết ví Apple Pay / Google Pay) · **B21:** cảnh báo Cục ATTT / Bộ Công an trên mps.gov.vn (mẫu mạo danh CIC) · **B23:** khuyến cáo chính thức trên vietcombank.com.vn (cú pháp 6167, hotline 1900 54 54 13) · Ngày xem: 27/11/2026 · **[CHỜ VŨ] link bài cụ thể + ngày xem của từng câu B19–B23** (cột `source` hiện mới ghi tên trang, chưa có link bài) |
| Xử lý những bước gì | B16–B18 viết lại thành dạng tin nhắn, không chép nguyên văn review · B19–B23 giữ nội dung tin mẫu, link đã làm vô hại / thay tên miền giả, bỏ SĐT · STK dạng `x...x889` |
| Số dòng / số đoạn | 8 câu · thuong 4 · kho 4 |
| Phiên bản / ngày lấy | Ngày xem 27/11/2026 |
| Nhãn | **thật** về kịch bản (review / cảnh báo có thật), câu chữ đã viết lại — ghi rõ ở cột `source` |
| Giới hạn | Chỉ gồm lừa đảo đã bị phát hiện và cảnh báo → thiếu biến thể mới · B16–B18 là diễn giải của nhóm từ lời kể, có thể lệch tin gốc |

## Dataset 4 · Tên miền lừa đảo giả danh ngân hàng / ví (`data/ten_mien_lua_dao.csv`)

| | |
|---|---|
| Dùng để làm gì | Nguồn cho công cụ `tra_ten_mien` (`codebase/tools.py`): link trong tin khớp danh sách → trả `"đã bị báo cáo lừa đảo"` |
| Từ đâu | Danh sách đen công khai của **tinnhiemmang.vn** (Trung tâm Giám sát an toàn không gian mạng quốc gia — NCSC): https://tinnhiemmang.vn/website-lua-dao, trang 2–40 (mới nhất xếp trước) |
| Xử lý những bước gì | Đọc trang 1–40, **chỉ giữ tên miền mà trang ghi "Mạo danh tổ chức" là 1 trong 11 app đã cào review** (Dataset 1); bỏ mục "Chưa xác định" và mục ghi chung "Viettel" (không rõ là Viettel Money) · **Làm vô hại:** mọi dấu `.` ghi thành `[.]` (công cụ đổi lại `.` trước khi so) · Không truy cập các tên miền lừa đảo · Kiểm: không trùng tên miền nào trong `eval/benchmark.csv` (tránh giấu đáp án câu thử vào dữ liệu công cụ) · Cột: `ten_mien, mao_danh, trang_thai, nguon, ngay_xem` |
| Số dòng / số đoạn | **27 tên miền:** MB 13 · MoMo 5 · Techcombank 4 · Vietcombank 2 · VietinBank 2 · TPBank 1 · không thấy BIDV, ZaloPay, Viettel Money, VNPAY, Cake trong 40 trang đã đọc |
| Phiên bản / ngày lấy | Ngày xem 27/11/2026 · cột `nguon` ghi URL trang (số trang trôi dần khi có báo cáo mới) · cột `trang_thai` chép nguyên chữ trên trang (Đã xử lý / Đang xử lý / Đang chờ; 2 dòng đầu không ghi) |
| Nhãn | **thật** (danh sách công khai của cơ quan nhà nước) · tên miền được AI (Claude Code) đọc từ trang nguồn, chỉ chép tên miền thấy trên trang, không tự sinh (`docs/ai-usage.md`) |
| Giới hạn | Chỉ 27 trong hàng chục nghìn mục của danh sách gốc (~6.000 trang) → công cụ sẽ trả `"không có trong dữ liệu"` cho hầu hết link lạ: **không có trong dữ liệu ≠ an toàn** · lệch về MB (13/27) · tên miền lừa đảo sống ngắn, danh sách cũ nhanh · nhiều mẫu đặt tên ngân hàng ở tên miền con (`tpbank.chamsockhachhang-…`) → không được nhận "chính thức" chỉ vì có tên ngân hàng trong link |

## Dataset 5 · Tên miền chính thức của ngân hàng / ví (`data/ten_mien_ngan_hang.csv`)

| | |
|---|---|
| Dùng để làm gì | Nguồn cho công cụ `tra_ten_mien`: host là tên miền này hoặc tên miền con của nó → trả `"tên miền chính thức"` |
| Từ đâu | Trang chủ của chính 11 tổ chức đã cào review (Vietcombank, MB, Techcombank, BIDV, VietinBank, TPBank, MoMo, ZaloPay, Viettel Money, VNPAY, Cake) |
| Xử lý những bước gì | Mở trang chủ, xác nhận tiêu đề / chân trang đúng tổ chức, ghi tên miền sau khi chuyển hướng (bỏ `www.`) · Cột: `ten_mien, to_chuc, nguon, ngay_xem, ghi_chu` |
| Số dòng / số đoạn | 11 tên miền |
| Phiên bản / ngày lấy | Ngày xem 27/11/2026 |
| Nhãn | **thật** · kiểm bằng AI đọc trang chủ; riêng `mbbank.com.vn` chặn truy cập tự động (403) nên được mở tay bằng trình duyệt và xác nhận ngày 27/11/2026 |
| Giới hạn | Mỗi tổ chức chỉ 1 tên miền chính; tổ chức có nhiều tên miền khác (tên miền phụ, cũ, chiến dịch) sẽ bị trả `"không có trong dữ liệu"` · tên miền chính thức **không** chứng minh tin nhắn là thật (kẻ gian có thể chèn link thật vào tin giả, hoặc dùng `@` trong URL) |