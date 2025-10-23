
# Start a new chat session
# app.py
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

api_key="GeminiAPIKEY"
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set.")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")
# In a real app, you'd manage chat sessions per user (e.g., using Flask's session object)
# For simplicity, we'll use a global chat object here, which is NOT suitable for multiple users.
# For multiple users, each user would need their own `model.start_chat()` session.
global_chat = model.start_chat(history=[])


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = global_chat.send_message(user_message)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Make sure to set GOOGLE_API_KEY environment variable
    app.run(debug=True)