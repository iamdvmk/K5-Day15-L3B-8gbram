import sys
from pathlib import Path

# Giống run.py: cho Python tìm thấy các module trong codebase/ (ai.py, tools.py, agent.py)
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "codebase"))

try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
except ImportError:
    pass

import streamlit as st
from agent import answer

st.set_page_config(page_title="Kiểm tin nhắn nghi lừa đảo")
st.title("Tin nhắn này có phải lừa đảo?")
st.caption("Chỉ kiểm nội dung tin nhắn / link. Không xác thực được người gửi. Bạn luôn tự quyết.")

msg = st.text_area("Dán tin nhắn nghi ngờ vào đây", height=150)
if st.button("Kiểm tra") and msg.strip():
    with st.spinner("Đang kiểm tra..."):
        out = answer(msg)["output"]
    for line in out.splitlines():
        if line.startswith("Mức rủi ro: Cao"):
            st.error(line)
        elif line.startswith("Mức rủi ro:"):
            st.warning(line) if "Trung bình" in line else st.success(line)
        else:
            st.write(line)