import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

st.set_page_config(page_title="My AI Chatbot", page_icon="🤖")

st.title("🤖 My AI Chatbot")

# Sidebar
st.sidebar.title("Settings")

personality = st.sidebar.selectbox(
    "Choose Personality",
    [
        "Normal Assistant",
        "Teacher",
        "Programmer",
        "Motivator",
        "Doctor"
    ]
)

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User Input
prompt = st.chat_input("Ask me anything...")

if prompt:

    if personality == "Teacher":
        prompt = "Answer like a friendly teacher.\n\n" + prompt

    elif personality == "Programmer":
        prompt = "Answer like an expert Python programmer.\n\n" + prompt

    elif personality == "Motivator":
        prompt = "Answer like a motivational speaker.\n\n" + prompt

    elif personality == "Doctor":
        prompt = "Answer like a professional doctor.\n\n" + prompt

    st.session_state.messages.append(
        {"role":"user","content":prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    answer = response.text

    st.session_state.messages.append(
        {"role":"assistant","content":answer}
    )

    with st.chat_message("assistant"):
        st.write(answer)