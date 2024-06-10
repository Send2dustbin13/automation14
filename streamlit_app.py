import streamlit as st

st.title("VIP NUMBERS")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.button("NUMBERS")
with col2:
    st.button('REQUEST')
with col3:
    st.button('REPORT')
with col4:
    st.button('SOLD')
with col5:
    st.button('ADD NO.')
        st.link("https://addpage.streamlit.app/")
with col6:
    st.button('SIGN IN')

