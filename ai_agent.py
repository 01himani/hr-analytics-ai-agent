import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-3.5-flash")


def ask_ai(image, kpis, question):

    if kpis:

        prompt = f"""
You are an HR Analytics AI Agent.

Important Instructions:
- Salary values shown in the dashboard or KPI summary are in Indian Rupees (₹).
- Never use "$" or "USD".
- Always use "₹" or "INR" when referring to salary.
- Use the dashboard image and KPI summary.

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

    else:

        prompt = f"""
You are an HR Analytics AI Agent.

Important Instructions:
- Analyze only the uploaded HR dashboard image.
- No HR dataset or KPI summary is available.
- Answer only from the dashboard.
- If information is not visible in the dashboard, say it cannot be determined.
- Never guess.
- Never use "$" or "USD".
- Use "₹" or "INR" only if salary values are visible.

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

    response = model.generate_content([prompt, image])

    return response.text
