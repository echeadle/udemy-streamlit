import streamlit as st 
from gpt4all import GPT4All

# Init the LLM Model
gpt = GPT4All(model_name="ggml-gpt4all-j-v1.2-jazzy.bin",model_path="/home/jcharis/.local/share/nomic.ai/GPT4All/")

# Create a storage
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
# st.write(st.session_state.messages)
for message in st.session_state.messages:
    with st.chat_message(message.get("role")):
        st.write(message.get("content"))


prompt = st.chat_input("Ask something")

if prompt:
    # Added to storage
    st.session_state.messages.append({"role": "user","content":prompt})
    # Display what was typed
    with st.chat_message("user"):
        st.write(prompt)

    # Process with LLM or NLP 
    result = gpt.chat_completion([{"role": "assistant","content":prompt}])
    st.write(result)
    response = result["choices"][0]["message"]["content"]

    # Store response
    st.session_state.messages.append({"role": "assistant","content":response})

     # Display Response from AI Chat
    with st.chat_message("assistant"):
        st.markdown(response)


   