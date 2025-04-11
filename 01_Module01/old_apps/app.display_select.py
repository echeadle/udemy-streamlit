# Core Packages
import streamlit as st


# Select/Multiple select
my_lang = ["Python", "Julia", "Go", "Rust"]

choice = st.selectbox("Language", my_lang)
st.write(f"You selected {choice}")

# Multiple Selection
spoken_lang = ("English", "French", "Spanish", "Twi")
my_spoken_lang = st.multiselect("Spoken Language", spoken_lang, default="English")

# Slider
# Numbers (Int/Float/Dates)
age = st.slider("Age",1,100)

# Any Datatype
# Select Slider
color = st.select_slider("Choose Color",options=["yellow", "red", "blue", "black", "white"], value=("yellow", "red"))