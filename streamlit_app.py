import streamlit as st

st.title("ADD NUMBER")

name = st.text_input("ENTER NUMBER")
email = st.date_input("ENTER DATE")
number = st.selectbox(SINGLE, DOUBLE, TRIPLE,placeholder="ENTER CATEGORY", label_visibility="visible")
checkbox = st.checkbox("Get latest news and updates...")

save = st.button("Submit")
cancel = st.button("Cancel")
if save:
  st.success("Submitted successfully !!!")
