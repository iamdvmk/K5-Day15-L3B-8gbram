# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Ôn lại: ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
> Repo chỉ chứa số đã tổng hợp và vài dòng ví dụ — không chép lại nguyên file data.

## 1. Cách đếm

- **Data dùng:** review công khai trên Google Play của 11 app ngân hàng / ví (MoMo, Vietcombank, MB Bank, Techcombank, BIDV, VietinBank, ZaloPay, TPBank, Viettel Money, VNPAY, Cake), `lang=vi`, `country=vn`. Mỗi app gộp 5.000 review mới nhất + 5.000 review "liên quan nhất", bỏ trùng theo `reviewId`. Lấy ngày 27/11/2026. Review khớp bộ lọc có ngày từ 30/08/2023 đến 26/11/2026.
- **Đếm gì:** số review mà người viết (hoặc người thân) kể **đã bị lừa / bị chiếm tài khoản**; trong đó đếm riêng loại **đúng lát cắt**: bị lừa qua tin nhắn / link / hướng dẫn của kẻ giả danh.
- **Trên tập nào, lọc gì:**
  1. Máy lọc theo từ khoá ngữ cảnh lừa đảo (`bị lừa`, `lừa đảo`, `mạo danh`, `tin nhắn lạ`, `link lạ`, `bị hack`, `chiếm đoạt`…) → 566 review, máy gợi ý nhóm ở cột `nhom_goi_y`.
  2. Người đọc tay từng review, gán `loai` và `dung_chu_de`: **1 chỉ khi người viết (hoặc người thân) đã bị lừa / suýt bị lừa / bị chiếm TK**; góp ý, nhận xét chung về lừa đảo, khen tính năng chống lừa → 0; không đủ thông tin → `mo_ho`, 0.
- **Mẫu số:** **70.294** review (tổng số review duy nhất kéo về được của 11 app), không phải số review khớp từ khoá.
- **Script / công thức:** `evidence/mine_reviews.py` (kéo + lọc → `evidence/reviews_matched.csv`). Đếm lại sau đọc tay:
  ```
  python -c "import csv,collections as c;r=list(csv.DictReader(open('evidence/reviews_matched.csv',encoding='utf-8-sig')));print(c.Counter((x['loai'],x['dung_chu_de']) for x in r))"
  ```
  Lưu ý: Google Play cập nhật review liên tục nên chạy lại script ở ngày khác sẽ ra mẫu số hơi khác. Mẫu số từng app ở bảng §3 lấy từ lần chạy ngày 27/11/2026.

## 2. Đọc trước, đếm sau

Đã đọc tay toàn bộ 566 review trong `reviews_matched.csv`. Các *kiểu* thấy được:
- **Chửi app là "lừa đảo"** vì lỗi giao dịch, trừ tiền không rõ lý do, phí ví trả sau, tự gia hạn, thưởng giới thiệu không về; hoặc góp ý chung về chống lừa — nhiều nhất, không phải bị lừa (`khong_lien_quan`: 444).
- **Nói về tính năng chống lừa của app** — phần lớn phàn nàn bắt gõ câu xác nhận, cảnh báo "ứng dụng giả mạo / trợ năng" khi đang cần chuyển tiền gấp; một số khen (`tinh_nang_chong_lua`: 65).
- **Cuộc gọi mạo danh** — ngoài phạm vi lát cắt (chỉ xử lý tin nhắn / link) (`cuoc_goi_ngoai_pham_vi`: 22).
- **Bị hack điện thoại / chiếm tài khoản** rồi mất tiền hoặc bị vay hộ (`bi_hack_chiem_tk`: 6).
- **Bị lừa kiểu khác** — lừa vay hộ, trung gian cho vay, nghi lộ thông tin cho kẻ lừa đảo… (`bi_lua_khac`: 14).
- **Nhận tin nhắn / link / hướng dẫn giả danh rồi làm theo** — đúng lát cắt (`goi_nhan_tin_link_gia_danh`: 2).
- Mơ hồ, không đủ thông tin để kết luận (`mo_ho`: 13).

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---|---|---|
| Review khớp bộ lọc từ khoá (máy) | 566 / 70.294 | 0,8% | chưa đọc tay |
| Trong số khớp, đọc tay đúng là chuyện bị lừa / bị chiếm TK | 22 / 566 | 3,9% | 96,1% khớp nhầm → bộ lọc từ khoá rất nhiễu |
| **Review kể bị lừa / bị chiếm TK** | **22 / 70.294** | **0,03%** | gồm 14 `bi_lua_khac` + 6 `bi_hack_chiem_tk` + 2 `goi_nhan_tin_link_gia_danh` |
| **Đúng lát cắt: bị lừa qua tin nhắn / link / hướng dẫn giả danh** | **2 / 70.294** | **0,003%** | dòng 208 (bấm link lạ), 519 (làm theo hướng dẫn kẻ lừa) |
| Cuộc gọi mạo danh (ngoài phạm vi, không tính) | 22 / 70.294 | 0,03% | |

Theo từng app (review kể bị lừa / bị chiếm TK, `dung_chu_de = 1`):

| App | x / N | App | x / N |
|---|---|---|---|
| MoMo | 4 / 6.539 | ZaloPay | 1 / 6.579 |
| Vietcombank | 3 / 6.167 | TPBank | 2 / 6.327 |
| MB Bank | 1 / 5.899 | Viettel Money | 4 / 5.838 |
| Techcombank | 2 / 5.955 | VNPAY | 0 / 8.661 |
| BIDV | 0 / 6.418 | Cake | 2 / 5.919 |
| VietinBank | 3 / 5.992 | | |

Ghi chú: 566 review khớp = 483 `co_the_bi_lua` + 19 cuộc gọi + 64 tính năng (theo gợi ý của máy ở cột `nhom_goi_y`; cột `loai` là nhãn đọc tay nên số từng nhóm khác một chút). Chạy lại script cùng ngày 27/11/2026 ra đúng cùng 566 review và cùng mẫu số 70.294.

## 4. ≥5 ví dụ cụ thể (mã dòng = số dòng trong `evidence/reviews_matched.csv`, đã bỏ tên người viết)

1. **Dòng 208** · Techcombank · 1★ · 24/09/2026 · đúng lát cắt — "vợ mình không biết kích vào link lạ từ lúc nào và đã mất hơn 500tr đồng bao gồm tiền gửi và tiền sử dụng tk cá nhân… Khi gọi phản ánh thì tổng đài cũng chỉ bảo trình báo công an và số tiền này khó lấy lại"
2. **Dòng 519** · Cake · 1★ · 05/01/2025 · đúng lát cắt — "Mình bị bọn lừa đảo báo vào app mở tk tín dụng ảo rồi nó bảo để hệ thống xóa. Không biết giờ sao tk bị sao rồi"
3. **Dòng 347** · TPBank · 1★ · 22/10/2024 · bị chiếm TK — "Ngày 16/10 tôi bị hack đt, sổ tiết kiệm của tôi ở ngân hàng ViB và TPbank bị bọn xấu vào tất toán và chuyển tiền đi"
4. **Dòng 387** · Viettel Money · 1★ · 28/08/2026 · bị chiếm TK — "mình bị hack đt thế là nó vào cake vp bank vay 40 triệu. giải ngân luôn… giờ hàng tháng điện thoại giục đóng lãi"
5. **Dòng 70** · MoMo · 1★ · 10/09/2026 · bị chiếm TK — "mất tiền từ momo bị hack mất 5trieu báo ngân hàg r"
6. **Dòng 475** · Cake · 4★ · 01/12/2025 · bị lừa khác — "ngân hàng thì cho vay nhanh nhưng gặp phải ng trung gian lừa đảo.lừa mất số tiền vừa vay xong"
7. **Dòng 415** · Viettel Money · 1★ · 19/11/2025 · bị lừa khác — "bị lừa vay tiền trên app này mà chả hiểu sao lại cho sinh viên vay 1 số tiền lớn như vậy"

## 5. Giới hạn của data

- **Review app không phải nơi người ta kể chuyện bị lừa.** Người dùng lên Play Store để chấm app (lỗi, phí, tốc độ), nên 0,03% / 0,003% là **cận dưới rất thấp**, không phải tỉ lệ người dùng gặp lừa đảo. Data cho thấy pain **có thật và thiệt hại lớn** (ví dụ mất hơn 500 triệu, bị vay hộ 40 triệu), nhưng **không đo được tần suất** (bao nhiêu người, bao nhiêu lần / tháng nhận tin giả).
- **Lệch về phía tiêu cực:** review 1★ chiếm đa số; người bị lừa nhưng không đổ lỗi cho app thì không viết review.
- **Bộ lọc từ khoá bỏ sót** review kể chuyện bị lừa mà không dùng từ khoá nào trong danh sách → chưa đo được tỉ lệ bỏ sót.
- **Một người đọc tay**, chưa có người thứ hai đọc lại để kiểm độ thống nhất của nhãn.
- **Mẫu không ngẫu nhiên:** gộp "mới nhất" + "liên quan nhất" theo thuật toán của Google Play.

→ **Kiểm lại bằng phỏng vấn / khảo sát:** hỏi khách hàng app ngân hàng / ví: 1 tháng qua nhận mấy tin nhắn / link mang danh ngân hàng đáng ngờ · lần gần nhất mất bao lâu để kiểm tra thật / giả · kiểm bằng cách nào · đã từng (hoặc suýt) làm theo chưa. Kết quả ghi ở `evidence/interviews/` và tổng hợp ở `evidence/summary.md`.
