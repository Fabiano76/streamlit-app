import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("💬 Professor GPT")
st.subheader("Ask me anything!")

# Input box
user_input = st.text_input("What do you want to learn?")

# If user enters input
if user_input:
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" if supported
            messages=[
                {"role": "system", "content": "You are a helpful AI professor."},
                {"role": "user", "content": user_input}
            ]
        )
        st.markdown("### 🤖 Response:")
        st.write(response.choices[0].message["content"])
