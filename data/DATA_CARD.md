# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Review Google Play về lừa đảo của app ngân hàng / ví (`evidence/reviews_matched.csv`)

| | |
|---|---|
| Dùng để làm gì | **Đào bằng chứng pain** (`evidence/data-mining.md`) · gốc kịch bản cho 3 câu thử `data_that` trong `eval/benchmark.csv` (B16, B17, B18 — tin nhắn được viết lại theo kịch bản người dùng kể trong review, không phải nguyên văn tin nhắn thật) |
| Từ đâu | Review công khai trên Google Play của 11 app: MoMo, Vietcombank, MB Bank, Techcombank, BIDV, VietinBank, ZaloPay, TPBank, Viettel Money, VNPAY, Cake (`lang=vi`, `country=vn`), kéo bằng thư viện `google-play-scraper` |
| Xử lý những bước gì | **Kéo:** mỗi app 5.000 review mới nhất + 5.000 "liên quan nhất", bỏ trùng theo `reviewId` → 70.294 review · **Lọc:** giữ review khớp từ khoá ngữ cảnh lừa đảo, máy gợi ý nhóm (`nhom_goi_y`) → 566 review · **Làm sạch:** bỏ xuống dòng trong nội dung · **Ẩn danh:** bỏ tên người viết, ảnh đại diện, `reviewId`; chỉ giữ app, số sao, ngày, nội dung · **Gán nhãn tay:** cột `loai` (7 nhóm) + `dung_chu_de` (1 = người viết / người thân đã bị lừa hoặc bị chiếm TK) · Script: `evidence/mine_reviews.py` |
| Số dòng / số đoạn | 566 review khớp từ khoá (trên tổng 70.294 review đã kéo) · 22 dòng `dung_chu_de = 1`, trong đó 2 dòng đúng lát cắt tin nhắn / link giả danh |
| Phiên bản / ngày lấy | Lấy ngày 27/11/2026 · review khớp có ngày từ 30/08/2023 đến 26/11/2026 · `google-play-scraper` 1.2.7 |
| Nhãn | **thật** (review công khai, đã ẩn danh) · nhãn `loai` / `dung_chu_de` do một thành viên đọc tay, có AI hỗ trợ rà lại (xem `docs/ai-usage.md`) |
| Giới hạn | Review dùng để chấm app nên phần lớn là phàn nàn lỗi / phí, rất ít người kể chuyện bị lừa → chỉ cho **cận dưới**, không đo được tần suất nhận tin giả · lệch về review 1★ · bộ lọc từ khoá bỏ sót review không dùng từ khoá trong danh sách · chỉ một người gán nhãn, chưa kiểm độ thống nhất · mẫu "liên quan nhất" do thuật toán Google Play chọn, không ngẫu nhiên · chạy lại ở ngày khác ra mẫu số hơi khác vì review mới liên tục |

**Data `synthetic` (nhóm tự sinh):** ghi cách sinh (prompt / script), seed, người kiểm, số dòng đã kiểm tay. Data tự dựng **không phải bằng chứng pain**.

## Dataset 2 · [tên — dữ liệu bản chạy thử đọc qua `codebase/tools.py`]

*(Chờ điền: hỏi Thành — công cụ của bản chạy thử đọc data gì, để ở `data/` file nào. Hỏi Vũ — các câu thử `tu_viet` trong `eval/benchmark.csv` dựa trên nguồn nào.)*
