from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)

examples = [
    ("hello", "Hello! How can I help you today?"),
    ("hi", "Hello! How can I help you today?"),
    ("bye", "Goodbye! Have a great day!")
]

questions = [q for q, a in examples]
answers = [a for q, a in examples]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def get_response(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    index = np.argmax(similarity)
    return answers[index]

@app.route("/")
def home():
    return "WhatsApp Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    reply = get_response(incoming_msg)
    response.message(reply)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
