from flask import Flask, render_template, request, jsonify
import requests, os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv("TOGETHER_API_KEY")

TOGETHER_URL = "https://api.together.xyz/inference"
MODEL = "mistralai/Mistral-7B-Instruct-v0.1"

def query_mistral(prompt, max_tokens=200):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "model": MODEL,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": 0.7,
    }

    try:
        response = requests.post(TOGETHER_URL, json=data, headers=headers)
        res_json = response.json()
        print("🧠 Mistral Response:", res_json)  # debug

        # Extract from nested structure: output -> choices -> [0] -> text
        output_data = res_json.get("output", {})
        choices = output_data.get("choices", [])
        if choices and "text" in choices[0]:
            return choices[0]["text"].strip()
        else:
            return "❌ No valid response generated."

    except Exception as e:
        print("❌ Error in query_mistral:", e)
        return "❌ Failed to connect to Mistral."


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    email = request.form["email"]
    tone = request.form["tone"]

    summary_prompt = (
        f"You are an assistant that summarizes professional emails.\n\n"
        f"Email:\n{email}\n\n"
        f"Please provide a clear and concise summary in 2–3 bullet points:"
    )

    reply_prompt = (
        f"You are an assistant that writes {tone.lower()} replies to emails.\n\n"
        f"Original Email:\n{email}\n\n"
        f"Write a complete reply to this email in a {tone.lower()} tone:"
    )


    summary = query_mistral(summary_prompt)
    reply = query_mistral(reply_prompt)

    return jsonify({"summary": summary, "reply": reply})

if __name__ == "__main__":
    app.run(debug=True)