import streamlit as st 
from gpt4all import GPT4All

# Init the LLM Model
gpt = GPT4All(model_name="mistral-7b-openorca.gguf2.Q4_0.gguf", 
              model_path="/home/echeadle/gpt4all/resources")

# Create storage for messages
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display chat history
# st.write(st.session_state.messages)
for message in st.session_state.messages:
    with st.chat_message(message.get("role")):
        st.write(message.get("content"))
    

prompt = st.chat_input("Ask a question")

if prompt:
    
    # Add the user prompt to the chat history
    st.session_state.messages.append({"role":"user","content": prompt})
    # Display what was typed
    with st.chat_message("user"):
        st.write(prompt)
        
        result = gpt.chat_session([{"role": "assistant","content":prompt}])
        response = result["choices"]["message"]["content"]
        st.write(response)
        st.session_state.messages.append({"role":"assistant","content": prompt})