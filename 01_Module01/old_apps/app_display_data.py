# Basics & Fundamentals

# Core Packages
import streamlit as st

# Load EDA Pkgs
import pandas as pd

# Display data

df = pd.read_csv("iris.csv")

# Method 1
# st.dataframe(df,500,400) <<Height, width
#st.dataframe(df)

# Adding a color sytle from pandas
st.dataframe(df.style.highlight_max(axis=0))

# Method 2: Static Table
#st.table(df)

# Method 3: Using superfnc st.write
st.write(df.head())

# Display Json
st.json({'data': "name"})

# Display Code
mycode = """
def sayhello():
    print("Hello Streamlit Lovers")
"""
st.code(mycode,language='python')