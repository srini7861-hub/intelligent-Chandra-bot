from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

@app.route("/")
def home():
    return "Intelligent Chandru Bot is running!"

@app.route("/send", methods=["GET"])
def send_message():
    msg = request.args.get("msg", "Hello Chandru!")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=payload)
    return "Message sent!" 