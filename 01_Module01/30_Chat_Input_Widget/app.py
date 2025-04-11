import streamlit as st 

# Create storage for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input("Ask Something")
if prompt:
    
    # Add the user prompt to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display the prompt message
    with st.chat_message("user"):
        st.write(prompt)
        
