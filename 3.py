import streamlit as st
import ollama

st.title("AI Chatbot")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat messages from session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Accept user input (must be outside the loop)
user_input = st.chat_input("Type your message")

if user_input:
    # Add user message to state & render immediately
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    with st.chat_message("user"):
        st.write(user_input)

    # Fetch response from Ollama
    response = ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )
    bot_response = response["message"]["content"]

    # Add bot response to state & render immediately
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })
    with st.chat_message("assistant"):
        st.write(bot_response)