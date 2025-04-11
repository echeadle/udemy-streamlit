# Core Packages
import streamlit as st

# Text Input
fname = st.text_input("Enter Firstname", max_chars=10)
st.title(fname)

# Password Input
password = st.text_input("Enter Password", type='password')
st.title(password)


# Text Area
message = st.text_area("Enter Message", max_chars=100, height=68)
st.write(message)

# Numbers
number = st.number_input("Enter Number", 0, 25, step=5)

# Date Input
my_app = st.date_input("Appointment")

# Time Input
my_time = st.time_input("My Time")

# Color Picker
color = st.color_picker("Select Color")