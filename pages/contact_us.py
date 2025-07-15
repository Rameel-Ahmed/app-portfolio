import streamlit as st 
st.header("Contact Me")

st.title("Streamlit Form Demo")
st.subheader("Enter details below")

# DOCUMENTATION >> st.help(st.form)

# CREATING OUR FORM FIELDS
with st.form("form1", clear_on_submit=True):
    name = st.text_input("Enter full name")
    email = st.text_input("Enter email")
    message = st.text_area("Message")
    

    submit = st.form_submit_button("Submit this form")
