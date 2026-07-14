import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

# -----------------------------
# MEMORY VAULT (Session State)
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# PAGE TITLE
# -----------------------------
st.title("🤖 MY AI MULTIVERSE CHATBOT")

# -----------------------------
# PERSONALITY SELECTOR
# -----------------------------
personality = st.selectbox(
    "Choose AI Personality",
    [
        "Normal Assistant",
        "Teacher",
        "Motivator",
        "Comedian",
        "Scientist",
        "Programmer"
    ]
)

# -----------------------------
# SHOW CHAT HISTORY
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# CHAT INPUT
# -----------------------------
if user_message := st.chat_input("Say something..."):

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_message)

    # Personality Prompt
    prompt = f"""
You are acting as a {personality}.

Reply according to this personality.

User: {user_message}
"""

    # Gemini Response
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    ai_response = response.text

    # Show assistant message
    with st.chat_message("assistant"):
        st.markdown(ai_response)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_response
        }
    )