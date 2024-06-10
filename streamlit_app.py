import streamlit as st

st.title("SIGN UP")

name = st.text_input("Enter Name")
email = st.text_input("Enter Email address")
number = st.text_input("Enter Mobile number")
checkbox = st.checkbox("Get latest news and updates...")

save = st.button("Submit")
cancel = st.button("Cancel")
if save:
  st.success("Submitted successfully !!!")
if cancel:
  st.error("Canceled successfully")
