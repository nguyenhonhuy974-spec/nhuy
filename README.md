
# Rule Converter - Streamlit App

Ứng dụng chuyển đổi chuỗi theo quy tắc do bạn cung cấp (phiên bản rút gọn).

## Cách dùng

1. Mở `app.py` bằng Streamlit:
```
streamlit run app.py
```
2. Dán văn bản vào ô **Đầu vào** → bấm **Xử Lý** → sẽ nhận **Đầu ra** ở dưới.  
3. Bấm **Sao chép nhanh** để copy kết quả vào clipboard (chạy trong trình duyệt).

## Những điều cần biết
- Số được công nhận là 1–3 chữ số. Quy tắc áp dụng cho các lệnh ngay sát sau số.  
- Lệnh hỗ trợ: `lo`/`lô` → `lo`; `d`/`đ` → `dau` (với số 1-2 chữ số) hoặc `d` (với 3 chữ số); `c` → `duoi` (1-2 chữ số) hoặc `cang` (3 chữ số); `dc` → luôn `dd`; `cuoi`/`cuối` → tương tự `c`.
- `kep` và `XXtoiYY` đã được loại bỏ theo yêu cầu.

## Deploy
- Bạn có push repository lên GitHub rồi deploy trên [Streamlit Cloud](https://share.streamlit.io/).

