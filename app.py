import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(page_title="IAASSE Academic Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 IAASSE Academic Chatbot")
st.write("Welcome! You can ask any academic or technical questions regarding the IAASSE platform here.")

# 2. API Key Configuration
GOOGLE_API_KEY = "AQ.Ab8RN6I0tIrW8VlFHJzIng3INDBVykOhrruy4SmcgA6GPxYy1g"

# Configure the Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# 3. System Instructions (Knowledge Base)
IAASSE_CONTEXT = """
You are the official academic chatbot for IAASSE. Your role is to assist users, researchers, and students based on the following strict knowledge base. Answer clearly, professionally, and briefly.
(هنا باقي نص الـ 50 سؤالاً كما هو في الكود السابق)
"""

# Initialize Model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=IAASSE_CONTEXT
)

# 4. Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Handle Input
if user_query := st.chat_input("Type your question here..."):
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            response = model.generate_content(user_query)
            full_response = response.text
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            message_placeholder.error(f"An error occurred: {e}")
