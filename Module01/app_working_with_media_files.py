# Core Packages
import streamlit as st

# Working Media FIles (video/images/audio)
# Display Images
# from PIL import Image
# img = Image.open("data/image_03.jpg")
# st.image(img, use_container_width=True)

# # From URL
# st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.serviceobjects.com%2Fblog%2Fwp-content%2Fuploads%2F2020%2F06%2Finnovation-and-science-concept-picture-id1177116437.jpg&f=1&nofb=1&ipt=931a8275fe1d1e0c88eb11744113613253bcf06fd6b4206f4a345bcdad039c46&ipo=images")


# Display Videos
# video_file = open("data/secret_of_success.mp4", "rb").read()
# st.video(video_file,start_time=3)

# Display Audio/Working with Audio
# start_time is in seconds
audio_file = open("data/song.mp3","rb").read()
st.audio(audio_file,start_time=90)
