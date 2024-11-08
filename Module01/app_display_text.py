import streamlit as st

# Working with and Displaying Text
st.text("Hello World this is a text")
name="Sammy"
st.text(f"This is so cool {name}")

# Header
st.header("This is a Header")

# Subheader
st.subheader("This is a subheader")

# Title
st.title("This is a title")

# Markdown
st.markdown("## This is markdown")

# Displaying Colored  Text/Bootstrap Alert
st.success("Successful")
st.warning("This is danger")
st.info("This is information")
st.error("This is an error")
st.exception("This is an exception")

# Superfunction
st.write("This is normal text")
st.write("## This is markdown text")
st.write(1+2)

st.write(dir(st))

# Help Info
st.help(range)