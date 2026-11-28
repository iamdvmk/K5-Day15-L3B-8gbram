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
from tools import redact_secrets

st.set_page_config(page_title="Kiểm tin nhắn nghi giả danh ngân hàng", page_icon="🛡️")

st.title("🛡️ Kiểm tin nhắn nghi giả danh ngân hàng")
st.caption(
    "Dán tin nhắn bạn vừa nhận. AI chấm mức rủi ro, chỉ dấu hiệu và gợi ý bước tiếp theo. "
    "Đừng dán mật khẩu hay mã OTP. Quyết định cuối cùng là của bạn."
)

def check_message():
    raw = st.session_state.message
    if not raw.strip():
        st.session_state.result = None
        return
    st.session_state.message = redact_secrets(raw)
    try:
        st.session_state.result = answer(raw)["output"]
        st.session_state.check_error = None
    except Exception as e:
        st.session_state.result = None
        st.session_state.check_error = f"Không gọi được model: {e}"


st.text_area("Nội dung tin nhắn", height=180, placeholder="Dán tin nhắn vào đây...", key="message")

if st.button("Kiểm tra", type="primary", on_click=check_message):
    if not st.session_state.message.strip():
        st.info("Hãy dán nội dung tin nhắn trước.")
if st.session_state.get("check_error"):
    st.error(st.session_state.check_error)
if st.session_state.get("result"):
    for line in st.session_state.result.splitlines():
        if not line.strip():
            continue
        if line.startswith("Mức rủi ro"):
            if "Cao" in line:
                st.error(line)
            elif "Trung bình" in line:
                st.warning(line)
            else:
                st.success(line)
        elif line.startswith("Dữ liệu nhạy cảm"):
            st.warning(line)
        else:
            st.markdown(line)
