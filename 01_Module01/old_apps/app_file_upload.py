# Core Packages
import streamlit as st

# File Processing Pkgs
from PIL import Image
import pandas as pd
import docx2txt
# import textract
from PyPDF2 import PdfReader
import pdfplumber

# Load Images
@st.cache_data
def load_image(image_file):
    img = Image.open(image_file)
    return img

def read_pdf(file):
    pdfReader = PdfReader(file)
    count = len(pdfReader.pages)
    all_page_text = ""
    for i in range(count):
        page = pdfReader.pages[i]
        all_page_text += page.extract_text()
    return all_page_text


def main():
    st.title("File Upload Tutorial")
    menu = ["Home", "Dataset", "DocumentFiles","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")
        image_file = st.file_uploader("Upload Images",
                                      type=["png","jpg","jpeg"])
        if image_file is not None:
            # To See Details
            # st.write(type(image_file))
            # Methods/Attrib
            # st.write(dir(image_file))
            file_details = {"filename":image_file.name,
            "filetype":image_file.type,"filesize":image_file.size}
            st.write(file_details)
            
            st.image(load_image(image_file=image_file),width=500)
        
    elif choice == "Dataset":
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload CSV", type=["csv"])
        if data_file is not None:
            #st.write(type(data_file))
            file_details = {"filename":data_file.name,
            "filetype":data_file.type,"filesize":data_file.size}
            st.write(file_details)
            df = pd.read_csv(data_file)
            st.dataframe(df)
            
            
    elif choice == "DocumentFiles":
        st.subheader("DocumentFiles")
        docx_file = st.file_uploader("Upload Document, ie pdf, docx or txt",
                        type=["pdf", "docx", "txt"])
        if st.button("Process"):
            if docx_file  is not None:
                file_details = {"filename":docx_file.name,
                "filetype":docx_file.type,"filesize":docx_file.size}
                st.write(file_details)
                if docx_file.type == "text/plain":
                    # Read as Bytes
                    # raw_text = docx_file.read()
                    # st.write(raw_text)
                    # st.text(raw_text) does not work as expected
                    # Read as string, decode bytes to string
                    raw_text = str(docx_file.read(), "utf-8")
                    st.write(raw_text) # works
                    #st.text(raw_text)  # works
    
                elif docx_file.type == "application/pdf":
                    # try:
                    #     with pdfplumber.open(docx_file) as pdf:
                    #         pages = pdf.pages[0]
                    #         st.write(pages.extract_text())
                    # except: 
                    #     st.write("None")
                    # Using PyPDF
                    raw_text = read_pdf(docx_file)
                    st.write(raw_text)
                    
                else:
                    raw_text = docx2txt.process(docx_file)
                    st.write(raw_text)
                    # st.text(raw_text)
    else:
        st.subheader("About")
        

    


if __name__ == '__main__':
    main()