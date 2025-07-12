# 📬 Email Summarizer + Reply Suggester

This is a simple, AI-powered web application that summarizes email content and generates professional replies based on tone and role — using Mistral 7B LLM via Together.ai API.

---

## ✨ Features

- 🔹 Summarizes emails into 2–3 bullet points
- 🔹 Suggests replies in different tones: Formal, Casual, or Assertive
- 🔹 Lets you specify the **role** you're replying as (e.g., Student, Manager, HR, etc.)
- 🔹 Clean, responsive frontend
- 🔹 Uses Mistral 7B model (free, open LLM via Together.ai)
- 🔹 Built using Flask + plain HTML/CSS + JavaScript

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **LLM API**: Mistral 7B via [Together.ai](https://platform.together.xyz/)
- **Prompt Engineering**: Role-based and tone-aware prompting
- **Security**: API key stored safely in `.env` file (not pushed to GitHub)

---

## 📁 Project Structure

email-assistant/

├── app.py                # Flask backend with API calls to Mistral 7B

├── templates/

│   └── index.html        # Frontend HTML form with styling and JS

├── .env                  # API key (excluded via .gitignore)

├── .gitignore            # Ignores env file and venv

├── requirements.txt      # Python dependencies

└── README.md             # You're reading it!

---

## 🧪 How to Run Locally

1. **Clone the repo** and navigate into it:

   ```bash
   ***


   git clone https://github.com/HarisNadeem471/email-assistant.git
   cd email-assistant

   **2. Set up a virtual environment**:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   Install dependencies:
   pip install -r requirements.txt

   **3. Set up your .env file:

   Create a .env file in the root directory:
   TOGETHER_API_KEY=your_api_key_here

   **4. Set up your .env file:
   Create a .env file in the root directory:
   TOGETHER_API_KEY=your_api_key_here

   **5. Run the app:
   python app.py

   **6. Visit: http://127.0.0.1:5000 in your browser

   ```

---
