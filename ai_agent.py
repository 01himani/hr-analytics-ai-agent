import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-3.5-flash")


def ask_ai(image, kpis, question):

    prompt = f"""
You are an HR Analytics AI Agent.

Important Instructions:
- The MonthlyIncome values are in Indian Rupees (₹).
- Never use "$" or "USD".
- Always use "₹" or "INR" for salary.
- Use only the dashboard image and KPI summary.

HR KPI Summary:

{kpis}

User Question:
{question}

Provide your response in this format:

Answer:
...

Business Insight:
...

Recommendation:
...
"""

    response = model.generate_content(
        [prompt, image]
    )

    return response.text