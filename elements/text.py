import streamlit as st

st.markdown("Markdown")
st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.caption("Caption")
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')
st.text("Text")
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")
