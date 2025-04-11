# Core Pkgs
import streamlit as st  
import streamlit.components as stc

# Utils
import base64
import pandas as pd
import time

# Functions
def text_downloader(raw_text):
    timestp = time.strftime("%Y%m%d-%H%M%S")  # Moved inside the function
    b64 = base64.b64encode(raw_text.encode()).decode()
    new_filename = f"new_text_file_{timestp}.txt"
    st.markdown("#### Download File ###")
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click Here!!</a>'
    st.markdown(href, unsafe_allow_html=True)
    
def csv_downloader(data):
    timestp = time.strftime("%Y%m%d-%H%M%S")  # Moved inside the function
    csvfile = data.to_csv(index=False)  # Corrected to `index=False`
    b64 = base64.b64encode(csvfile.encode()).decode()
    new_filename = f"new_csv_file_{timestp}.csv"
    st.markdown("#### Download File ###")
    href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!!</a>'
    st.markdown(href, unsafe_allow_html=True)
    
# Class
class FileDownloader(object):
    """docstring for FileDownloader
    >>> download = FileDownloader(data,filename,file_ext,file_ext='txt')
    """
    def __init__(self, data, filename='myfile',file_ext='txt'):
        super(FileDownloader, self).__init()
        self.data = data
        self.filename = filename
        self.file_ext = file_ext
        
    def download(self):
        timestp = time.strftime("%Y%m%d-%H%M%S")  # Moved inside the function
        b64 = base64.b64encode(self.data.encode()).decode()
        new_filename = f"{self.filename}_{timestp}_.{self.file_ext}"
        st.markdown("#### Download File ###")
        href = f'<a href="data:file/{self.file_ext};base64,{b64}" download="{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)

    
# Main App

def main():
    menu = ["Home", "CSV", "About"]
    
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Home")
        my_text = st.text_area("Your message")
        if st.button("Save"):
            st.write(my_text)
            # text_downloader(my_text)
            download = FileDownloader(my_text).download()
            
    elif choice == "CSV":
        try:
            df = pd.read_csv("../iris.csv")  # Adjust path if needed
            st.dataframe(df)
            csv_downloader(df)
        except FileNotFoundError:
            st.error("CSV file not found. Please check the file path.")
    
    else:
        st.subheader("About")
        
if __name__ == '__main__':
    main()
