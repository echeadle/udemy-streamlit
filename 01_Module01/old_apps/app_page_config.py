# Core Packages
import streamlit as st
from PIL import Image
# img = Image.open("jcharistechlogo.png")
# Must be the first activity, to change the tab icon
# Method 1:
# st.set_page_config(page_title='hello',
#                    page_icon=':smiley:',
#                    layout='wide',
#                    initial_sidebar_state='collapsed')

# Method 2: Dictionary
PAGE_CONFIG = {"page_title":"Hello","page_icon":":smiley:","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

# Additional Pkgs

# Funcs



def main():
    """All code goes here"""
    st.title("Hello Streamlit Lovers 🚀")
    st.sidebar.success("Menu")

if __name__ == '__main__':
    main()