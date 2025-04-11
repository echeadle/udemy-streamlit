# Core Pkgs
import streamlit as st 
import pandas as pd


def main():
    st.title("Streamlit Forms and Salary Calculator")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Forms Tutorial")
        
        # Salary Calculator
        # Combine Forms + columns
        with st.form(key='salaryform'):
            col1,col2,col3 = st.columns([3,2,1])
            with col1:
                amount = st.number_input("Hourly Rate in $")
                
            with col2:
                hours_per_week = st.number_input("Hours per week", 1,120)
            
            with col3:
                st.text("Salary")
                submit_salary = st.form_submit_button(label='Calculate')
                
        if submit_salary:
            with st.expander("Results"):
                daily = [amount * 8]
                weekly = [amount * hours_per_week]
                df = pd.DataFrame({'hourly': amount, 'daily':daily,'weekly':weekly})
                st.dataframe(df.T) # .T tranposes the values
        
        # Method 1: Context Manager
        with st.form(key='form1'):
            firstname = st.text_input("Firstname", key='firstname')
            lastname  = st.text_input("Lastname", key='lastname')
            dob = st.date_input("Date of Birth", key='dob')
    
            submit_button = st.form_submit_button(label='SignUp')
            
        # Results can be either inside form or outside of the form
        if submit_button:
            st.success(f"Hello {firstname} you have created an account.")
            
        # Method 2:
        form2 = st.form(key='form2')
        username = form2.text_input("Username", key='username')
        jobtype = form2.selectbox("Job", ["Dev", "Data Scientist", "Doctor"], key='jobtype')
        submit_button2 = form2.form_submit_button("Login")

        if submit_button2:
            st.write(username.upper())
    else:
        st.subheader("About")
        
        
if __name__ == '__main__':
    main()
