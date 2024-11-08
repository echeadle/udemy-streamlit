# Core Packages
import streamlit as st

# Working with Widgets
# Buttons/Radio/Checkbox/

# Working with Buttons
name = "Jesse"

if st.button("Submit"):
    st.write(f"Name: {name.upper()}")

if st.button("Submit", key='new02'):
    st.write(f"Name: {name.lower()}")
    
# Working with RadioButtons
status = st.radio("What is your status", ("Active", "Inactive"))

if status == 'Active':
    st.success("You are active")
elif status == "Inactive":
    st.warning("Inactive")
    
# Working with Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing Something")
    
# Working with Beta Expander
with st.expander("Python"):
    st.success("Hello Python")
    
with st.expander("Julia"):
     st.text("Hello Julia")