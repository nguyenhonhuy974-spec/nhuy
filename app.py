import streamlit as st
import json
from rules import apply_rules

st.set_page_config(page_title="Rule Converter", page_icon="🧾", layout="centered")
st.title("Rule Converter — xử lý theo rules.txt (phiên bản rút gọn)")

st.markdown("""
**Hướng dẫn ngắn:** Dán đoạn văn cần xử lý vào ô *Đầu vào*, bấm **Xử Lý** để nhận *Đầu ra*.  
Nút **Sao chép nhanh** sẽ copy kết quả vào clipboard trình duyệt.
""")

input_text = st.text_area("Đầu vào", height=220)

if st.button("Xử Lý"):
    output = apply_rules(input_text)
    st.text_area("Đầu ra", value=output, height=220, key="output_area")

    # JS copy button (uses navigator.clipboard)
    safe_text = json.dumps(output)  # ensure correct JS string escaping
    copy_js = f"""
    <script>
    function copyResult() {{
        const text = {safe_text};
        navigator.clipboard.writeText(text).then(function() {{
            const el = document.getElementById("copy-notice");
            if (el) el.innerText = "✅ Đã sao chép vào clipboard";
        }}, function(err) {{
            alert("Không thể sao chép vào clipboard: " + err);
        }});
    }}
    </script>
    <button onclick="copyResult()" style="margin-top:10px;">📋 Sao chép nhanh</button>
    <span id="copy-notice" style="margin-left:12px;color:green"></span>
    """
    st.markdown(copy_js, unsafe_allow_html=True)

# show small footer
st.markdown("---")
st.markdown("Phiên bản xử lý: số gốc 1-3 chữ số; lệnh: lo, d/đ, c, dc, cuoi. (Đã loại bỏ `kep` và `toi→den`).")
