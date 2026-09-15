import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-3.6-flash")

# Page setup
st.title("AI Text Summarizer")
st.write("Paste any text below and get a quick summary.")

# Input box
text = st.text_area("Your text", height=200)

# Button
if st.button("Summarize"):
    if text.strip() == "":
        st.warning("Please paste some text first.")
    else:
        with st.spinner("Summarizing..."):
            response = model.generate_content(f"Summarize this in 3 sentences:\n\n{text}")
        st.subheader("Summary")
        st.write(response.text)