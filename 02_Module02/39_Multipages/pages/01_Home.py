
import streamlit as st 



# Sharing variables among pages
#from app import my_variable


st.subheader("Home")

#st.write(my_variable)

st.write(st.session_state['my_calc'])
