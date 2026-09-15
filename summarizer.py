import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.6-flash")

text = input("Paste the text you want summarized:\n")

response = model.generate_content(f"Summarize this in 3 sentences:\n\n{text}")

print("\n--- Summary ---")
print(response.text)