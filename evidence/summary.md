# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).

## 1. Nguồn đã dùng

| Nguồn | Trạng thái | Ngưỡng |
|---|---|---|
| **Đào data** — review Google Play 11 app ngân hàng / ví | **Đạt ngưỡng** | x/N + % · cách chọn mẫu và cách đếm ghi trước (`data-mining.md`) · script `mine_reviews.py` chạy lại được · ≥5 ví dụ nguyên văn |
| Số liệu / cảnh báo công khai (ngân hàng, VNCERT, Bộ Công an) | Dùng để đối chiếu kênh tin nhắn / link | Có link + ngày xem |
| Phỏng vấn | Không dùng | — |
| Khảo sát | Không dùng | — |

**Cách chọn mẫu và cách đếm (đào data):** kéo review công khai trên Google Play của 11 app ngân hàng / ví (MoMo, Vietcombank, MB Bank, Techcombank, BIDV, VietinBank, ZaloPay, TPBank, Viettel Money, VNPAY, Cake), mỗi app 5.000 mới nhất + 5.000 "liên quan nhất", bỏ trùng → **70.294 review** (lấy ngày 27/11/2026) → lọc từ khoá ngữ cảnh lừa đảo → **566 review** → đọc tay từng review, gán `loai` + `dung_chu_de` (1 = người viết / người thân đã bị lừa, suýt bị lừa hoặc bị chiếm tài khoản). Chi tiết, tiêu chí và lệnh đếm lại: `evidence/data-mining.md` §1.

## 2. Số chính

- **Đào data:**
  - Trong 566 review có nhắc tới lừa đảo, chỉ **22/566 (3,9%)** là người kể đã bị lừa / bị chiếm tài khoản — 96% còn lại dùng chữ "lừa đảo" để chửi lỗi app, phí, tự trừ tiền, hoặc góp ý chung.
  - Trên toàn bộ review đã kéo: **22/70.294 (0,03%)**. Theo loại: 14 bị lừa kiểu khác (lừa vay hộ, trung gian cho vay, nghi lộ thông tin) · 6 bị hack điện thoại / chiếm tài khoản · **2 đúng lát cắt** (bị lừa qua link / hướng dẫn của kẻ giả danh) = **2/70.294 (0,003%)**.
  - Theo app (`dung_chu_de = 1`): MoMo 4 · Viettel Money 4 · Vietcombank 3 · VietinBank 3 · Techcombank 2 · TPBank 2 · Cake 2 · MB Bank 1 · ZaloPay 1 · BIDV 0 · VNPAY 0 (mẫu số từng app ở `data-mining.md` §3).
  - **65/566 (11,5%) review nói về tính năng chống lừa / cảnh báo giả mạo của chính app**, 55/65 chấm 1–2★ — chủ yếu bị chặn khi đã tắt trợ năng, bị báo "ứng dụng giả mạo / độc hại" nhầm, không vào được app lúc cần chuyển tiền. Nhiều hơn gần 3 lần số review kể bị lừa (22).
  - 22/566 review kể cuộc gọi mạo danh — ngoài phạm vi lát cắt, không tính.

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

Mã dòng = số dòng trong `evidence/reviews_matched.csv`. Mỗi trích dẫn ≤ 2 câu, giữ nguyên chính tả, `[…]` = phần đã bỏ. Link = trang app trên Google Play, xem ngày 27/11/2026.

1. "Vừa rồi vợ mình không biết kích vào link lạ từ lúc nào và đã mất hơn 500tr đồng bao gồm tiền gửi và tiền sử dụng tk cá nhân. […] Khi gọi phản ánh thì tổng đài cũng chỉ bảo trình báo công an và số tiền này khó lấy lại thật sự mất niềm tin" — dòng 208 · Techcombank · 1★ · 24/09/2026 · [link](https://play.google.com/store/apps/details?id=vn.com.techcombank.bb.app&hl=vi) · *đúng lát cắt*
2. "Mình bị bọn lừa đảo báo vào app mở tk tín dụng ảo rồi nó bảo để hệ thống xóa. Không biết giờ sao tk bị sao rồi" — dòng 519 · Cake · 1★ · 05/01/2025 · [link](https://play.google.com/store/apps/details?id=xyz.be.cake&hl=vi) · *đúng lát cắt*
3. "Ngày 16/10 tôi bị hack đt, sổ tiết kiệm của tôi ở ngân hàng ViB và TPbank bị bọn xấu vào tất toán và chuyển tiền đi, cùng khi đó bên tài khoản vietinbank thì không bị sao." — dòng 347 · TPBank · 1★ · 22/10/2024 · [link](https://play.google.com/store/apps/details?id=com.tpb.mb.gprsandroid&hl=vi) · *bị chiếm tài khoản*
4. "mình bị hack đt thế là nó vào cake vp bank vay 40 triệu. […] giờ hàng tháng điện thoại giục đóng lãi" — dòng 387 · Viettel Money · 1★ · 28/08/2026 · [link](https://play.google.com/store/apps/details?id=com.bplus.vtpay&hl=vi) · *bị chiếm tài khoản*
5. "ngân hàng thì cho vay nhanh nhưng gặp phải ng trung gian lừa đảo.lừa mất số tiền vừa vay xong..đã khó khăn càng khó khăn .k biết nói chi luôn" — dòng 475 · Cake · 4★ · 01/12/2025 · [link](https://play.google.com/store/apps/details?id=xyz.be.cake&hl=vi) · *bị lừa kiểu khác*
6. "mono lz mất tiền từ momo bị hack mất 5trieu báo ngân hàg r. đme quá sợ momo này" — dòng 70 · MoMo · 1★ · 10/09/2026 · [link](https://play.google.com/store/apps/details?id=com.mservice.momotransfer&hl=vi) · *bị chiếm tài khoản*
7. "app đểu app bắt gỡ ứng dụng giả mạo(mes ,Instagram) gỡ xong vẫn không cho vô app app như..." — dòng 166 · MB Bank · 1★ · 06/11/2026 · [link](https://play.google.com/store/apps/details?id=com.mbmobile&hl=vi) · *tính năng chống lừa chặn nhầm (không phải bằng chứng bị lừa — dùng cho thiết kế, xem §5)*

## 4. Các nguồn có khớp nhau không

**Data nói:** pain bị lừa qua tin nhắn / link giả danh **có thật và thiệt hại rất lớn** (mất hơn 500 triệu, bị vay hộ 40 triệu, người bị lừa không lấy lại được tiền và tổng đài chỉ khuyên trình báo công an), nhưng **rất hiếm xuất hiện trong review app**: 2/70.294. Review app ngân hàng là nơi người ta chấm app, không phải nơi kể chuyện bị lừa → data **không đo được tần suất** (bao nhiêu người, bao nhiêu lần / tháng nhận tin giả, mất bao lâu để tự kiểm).

- **Khớp:** kênh tin nhắn / link giả danh ngân hàng là thủ đoạn thật — Vietcombank, Cục ATTT / Bộ Công an đã công bố cảnh báo với tin mẫu và tên miền giả (link ở cột `source` của B19–B23 trong `eval/benchmark.csv`).
- **Lệch:** review cho thấy kênh này rất ít được kể (2/22) → không dùng review để khẳng định tần suất; chỉ dùng để khẳng định **mức độ nghiêm trọng** khi bị lừa.

## 5. Kết luận

**Giả thuyết đúng một phần — phải đổi cách đo tần suất.**
- **Đúng:** pain có thật và rất đắt — 22/566 (3,9%) review đã đọc tay kể người viết / người thân bị lừa hoặc bị chiếm tài khoản, rải ở 9/11 app; có ca mất hơn 500 triệu.
- **Không đúng như kỳ vọng:** chỉ 2/22 nói đúng kênh tin nhắn / link giả danh ngân hàng. Review là nơi chấm app nên ít người kể chuyện bị lừa qua tin nhắn → review chỉ cho **cận dưới**, không đo được tần suất nhận tin giả.
- **Đổi:** tần suất (bao nhiêu tin đáng ngờ / người / tháng) dùng ở `spec.md` §2 và persona chi phí là *(tự ước tính)*, ghi rõ trong spec.

Điều data vẫn cho thấy:
- Khi bị lừa thì **thiệt hại lớn và gần như không lấy lại được** → bỏ sót một tin lừa đắt hơn nhiều so với báo nhầm (khớp lựa chọn ở canvas dòng 6: ưu tiên không bỏ sót).
- **Cảnh báo chống lừa hiện có của app bị phàn nàn nhiều hơn chính chuyện bị lừa** (65 so với 22 review, 55/65 chấm 1–2★): chặn nhầm, bắt tắt trợ năng, không vào được app lúc cần → cảnh báo của nhóm phải **giải thích dấu hiệu cụ thể và để người dùng tự quyết**, không chặn thao tác.

Điều vẫn chưa biết: bao nhiêu khách hàng nhận tin / link giả danh ngân hàng mỗi tháng · họ tự kiểm bằng cách nào và mất bao lâu · bao nhiêu người từng (suýt) làm theo → hỏi ở phỏng vấn P1–P3.

Người viết review thường là người đang bực (lệch 1★) · bộ lọc từ khoá bỏ sót review không dùng từ trong danh sách · nhãn do 1 người gán · không có phỏng vấn / khảo sát kiểm lại tần suất.