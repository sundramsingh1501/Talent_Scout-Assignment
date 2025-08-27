import streamlit as st
from bot import ChatBot
from utils import format_response

st.set_page_config(page_title="AI Technical Interviewer", page_icon="🤖", layout="centered")

st.title("🤖 AI Technical Interviewer")
st.markdown("Transform your interview experience with our AI-powered technical assessment platform.")

if "chatbot" not in st.session_state:
    st.session_state.chatbot = ChatBot()
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Type your message here...")

if user_input:
    bot = st.session_state.chatbot
    response = bot.chat(user_input)

    st.session_state.history.append(("user", user_input))
    st.session_state.history.append(("assistant", response))

for role, msg in st.session_state.history:
    if role == "user":
        with st.chat_message("user"):
            st.write(msg)
    else:
        with st.chat_message("assistant"):
            st.write(format_response(msg))
