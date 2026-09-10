import os
import streamlit as st
from huggingface_hub import InferenceClient

st.title("🤖 AI Question Answering")

question = st.text_input("Enter your question:")

if st.button("Ask AI"):

    if question.strip():

        client = InferenceClient(
            api_key=os.environ["HF_TOKEN"]
        )

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        st.subheader("AI Answer")
        st.write(response.choices[0].message.content)

    else:
        st.warning("Please enter a question.")