# Core Pkgs
import streamlit as st

pages = [
    # st.Page("app.py"),
    st.Page("pages/01_Home.py", title="Home"),
    st.Page("pages/02_eda.py", title="EDA"),
    st.Page("pages/03_About.py", title="ABOUT"), 
]

my_variable = "From Main App.py Page"
my_calc = "This is from EDA.py"
st.session_state['my_variable'] = my_variable
st.session_state['my_calc'] = my_calc

def main():
    st.title("Streamlit Multi Page App")
    st.subheader("Main Page")
    st.write(my_variable)


if __name__ == '__main__':
    main()