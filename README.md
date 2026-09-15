# AI Text Summarizer

A simple web app that summarizes any pasted text into 3 concise sentences, powered by Google's Gemini API.

## Features
- Paste any text and get an instant AI-generated summary
- Clean, simple web interface built with Streamlit
- Uses Gemini 3.6 Flash for fast, accurate summarization

## Tech Stack
- Python
- Google Gemini API (`google-generativeai`)
- Streamlit (web UI)
- python-dotenv (environment variable management)

## Setup
1. Clone this repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it and install dependencies:pip install -r requirements.txt
4. Create a `.env` file (see `.env.example`) and add your own Gemini API key
5. Run the app:streamlit run app.py


## What I Learned
- Working with LLM APIs (Gemini) for real-world tasks
- Managing environment variables and API keys securely
- Debugging Python environment/dependency issues (venv vs global installs)
- Building and deploying a simple web app with Streamlit

## Live Demo
[https://ai-summarizer-hplddsn9fgbgfv5xptbq9e.streamlit.app/]