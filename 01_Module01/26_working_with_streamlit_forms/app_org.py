# Core Pkgs
import streamlit as st 
import pandas as pd


def main():
    st.title("Streamlit Forms and Salary Calculator")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Forms Tutorial")
        
        # Method 1: Context Manager
        with st.form(key='form1'):
            firstname = st.text_input("Firstname")
            lastname  = st.text_input("Lastname")
            dob = st.date_input("Date of Birth")
    
            submit_button = st.form_submit_button(label='SignUp')
            
        # Results can be either inside form or outside of the form
        if submit_button:
            st.success(f"Hello {firstname} you have created an account.")
            
        # Method 2:
        form2 = st.form(key='form2')
        username = form2.text_input("Username")
        jobtype = form2.selectbox("Job",["Dev", "Data Scientist", "Doctor"])
        submit_button2 = form2.form_submit_button("Login")
    
    else:
        st.subheader("About")
        
        
if __name__ == '__main__':
    main()