def get_response(msg):
    msg = msg.lower()

    # Salamu
    if msg in ["hi", "hello", "mambo", "habari"]:
        return """Karibu 👋
Tunatoa huduma za kidigitali kwa kiwango cha juu:

📌 Business Branding  
📌 Social Media Management  
📌 Printing Services  
📌 Graphic Design  
📌 Web Design  
📌 Domain & Hosting  
📌 Digital Marketing  
📌 ICT Solutions  

Chagua huduma unayotaka kwa kuandika jina lake."""

    # Branding
    elif "branding" in msg:
        return "Tunakusaidia kujenga brand yako 🔥\nLogos, identity, na muonekano wa biashara yako."

    # Social Media
    elif "social" in msg:
        return "Tunamanage kurasa zako za mitandao 📱\nContent, posting na growth ya followers."

    # Printing
    elif "printing" in msg:
        return "Tunaprint:\n✔ T-shirt\n✔ Banners\n✔ Business cards\n✔ Stickers\n\nUnahitaji ipi?"

    # Graphic Design
    elif "design" in msg:
        return "Tunatengeneza designs za kisasa 🎨\nLogos, posters, flyers na zaidi."

    # Website
    elif "web" in msg or "website" in msg:
        return "Tunatengeneza website za kisasa 🌐\nBiashara, kampuni na personal sites."

    # Hosting
    elif "hosting" in msg or "domain" in msg:
        return "Tunauza domains na hosting 🚀\nTunakuunganisha online haraka na salama."

    # Marketing
    elif "marketing" in msg:
        return "Digital Marketing 📢\nFacebook Ads, Instagram Ads na Google Ads."

    # ICT
    elif "ict" in msg:
        return "Tunatoa ICT Solutions 💻\nSoftware, support na ushauri wa kitaalamu."

    # Default
    else:
        return """Samahani sijakuelewa 😅

Chagua huduma:
✔ Branding
✔ Social Media
✔ Printing
✔ Design
✔ Website
✔ Hosting
✔ Marketing
✔ ICT"""
