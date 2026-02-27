from flask import Flask, request, jsonify, render_template
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    user_message = data["message"]

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=user_message
    )

    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)
