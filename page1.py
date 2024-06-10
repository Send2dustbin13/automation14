import streamlit as st

st.title("ADD NUMBER")
number = st.text_input("NUMBER")
date = st.date_input("DATE")
number = st.text_input("CATEGORY")
price = st.text_input("PRICE")

save = st.button("SUBMIT")
if save:
  st.success("SUBMITTED SUCCESSFULLY !!!")

