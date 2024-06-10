import streamlit as st

st.title("VIP NUMBERS")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.button('REQUEST')
with col2:
    st.button('REPORT')
with col3:
    st.button('DELETE NO.')
with col4:
    st.button('ADD NO.')
with col5:
    st.button('SIGN IN')

