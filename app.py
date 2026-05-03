from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

def get_response(msg):
    msg = msg.lower()

    if msg in ["hi", "hello", "mambo", "habari"]:
        return """Karibu 👋
Tunatoa huduma hizi:

1. Branding
2. Social Media
3. Printing
4. Design
5. Website
6. Hosting
7. Marketing
8. ICT

Andika huduma unayotaka."""

    elif "branding" in msg:
        return "Tunafanya Business Branding 🔥 (logo, identity, brand setup)."

    elif "social" in msg:
        return "Tunamanage social media 📱 (posts, growth, ads)."

    elif "printing" in msg:
        return "Tunaprint T-shirt, banners, cards, stickers."

    elif "design" in msg:
        return "Graphic Design 🎨 (logos, posters, flyers)."

    elif "website" in msg or "web" in msg:
        return "Tunatengeneza website za kisasa 🌐."

    elif "hosting" in msg or "domain" in msg:
        return "Tunatoa domain & hosting 🚀."

    elif "marketing" in msg:
        return "Tunafanya digital marketing 📢 (FB, IG, Google Ads)."

    elif "ict" in msg:
        return "Tunatoa ICT solutions 💻 (support, systems)."

    else:
        return "Samahani 😅 Andika: Branding, Social, Printing, Design, Website, Hosting, Marketing au ICT."

@app.route("/", methods=["GET"])
def home():
    return "WhatsApp Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get('Body', '')
    resp = MessagingResponse()
    msg = resp.message()
    reply = get_response(incoming_msg)
    msg.body(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
