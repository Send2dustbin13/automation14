import streamlit as st

st.title("ADD NUMBER")
number = st.text_input("NUMBER")
date = st.date_input("DATE")
number = st.text_input("CATEGORY")
price = st.number_input("PRICE")

save = st.button("SUBMIT")
if save:
  st.success("Submitted successfully !!!")
