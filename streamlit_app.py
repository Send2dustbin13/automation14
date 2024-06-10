import streamlit as st

st.title("ADD NUMBER")
number = st.text_input("NUMBER")
date = st.date_input("DATE", format = DD/MM/YYYY)
number = st.text_input("CATEGORY")
price = st.number_input("PRICE")

save = st.button("Submit")
if save:
  st.success("Submitted successfully !!!")
