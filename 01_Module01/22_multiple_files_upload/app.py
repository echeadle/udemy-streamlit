import os
import streamlit as st 

from PIL import Image

@st.cache_data
def load_image(imagefile):
    img = Image.open(imagefile)
    return img

def save_uploaded_file(uploadedfile):
    with open(os.path.join("tempDir",uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
        
        return st.success(f"Saved {uploadedfile.name} to tempDir")
        
    
def main():
    st.title("Multiple File Uploads App")
    
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu )
    
    if choice == "Home":
        st.subheader("Upload Multiple Files")
        
        uploadedfiles = st.file_uploader("Upload Multiple Images",type=["png",'jpeg','jpg'],accept_multiple_files=True)
        if uploadedfiles is not None:
            st.write(uploadedfiles) #List
            for imagefile in uploadedfiles:
                st.write(imagefile.name)
                st.image(load_image(imagefile), width=250)
                # Save Individual file
                save_uploaded_file(imagefile)    
    else:
        st.subheader("About App")
        
if __name__ == '__main__':
    main()