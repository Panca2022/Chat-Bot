from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv
import webbrowser
import threading
import time

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)

# Flag to check if the browser is already opened
browser_opened = False

@app.route('/')
def home():
    return "AI Chatbot is running!"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No Message Provided"}), 404

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"User:{user_input}\nAI:",
            max_tokens=150,
            temperature=0.7
        )
        reply = response.choices[0].text.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Open the browser only once when the app starts
def open_browser():
    global browser_opened
    if not browser_opened:
        time.sleep(2)  # Wait for the Flask app to fully start
        webbrowser.open("http://127.0.0.1:5000/")
        browser_opened = True

if __name__ == '__main__':
    # Run the browser opening in a separate thread to avoid blocking the main app
    threading.Thread(target=open_browser).start()

    # Run the Flask app without debug for production-like behavior (comment out to enable debugging)
    app.run(debug=True, use_reloader=False)  # Disable Flask's auto-reloader, so the browser doesn't open multiple times
