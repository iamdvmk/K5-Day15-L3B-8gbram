"""Giao diện demo Streamlit — Track E, nhóm 8gbram.

Chạy: python -m streamlit run app.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "codebase"))

try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
except ImportError:
    pass

import streamlit as st
from agent import answer

st.set_page_config(page_title="Kiểm tin nhắn nghi giả danh ngân hàng", page_icon="🛡️")

st.title("🛡️ Kiểm tin nhắn nghi giả danh ngân hàng")
st.caption(
    "Dán tin nhắn bạn vừa nhận. AI chấm mức rủi ro, chỉ dấu hiệu và gợi ý bước tiếp theo. "
    "Đừng dán mật khẩu hay mã OTP. Quyết định cuối cùng là của bạn."
)

msg = st.text_area("Nội dung tin nhắn", height=180, placeholder="Dán tin nhắn vào đây...")

if st.button("Kiểm tra", type="primary"):
    if not msg.strip():
        st.info("Hãy dán nội dung tin nhắn trước.")
    else:
        with st.spinner("Đang kiểm tra..."):
            try:
                output = answer(msg)["output"]
            except Exception as e:
                st.error(f"Không gọi được model: {e}")
                st.stop()

        for line in output.splitlines():
            if not line.strip():
                continue
            if line.startswith("Mức rủi ro"):
                if "Cao" in line:
                    st.error(line)
                elif "Trung bình" in line:
                    st.warning(line)
                else:
                    st.success(line)
            else:
                st.markdown(line)
