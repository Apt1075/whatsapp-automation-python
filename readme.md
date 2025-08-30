# 📩 Twilio WhatsApp Message Sender

A simple Python script to send WhatsApp messages using the [Twilio API](https://www.twilio.com/).  

## 🚀 Features
- Send WhatsApp messages directly from Python.
- Easy-to-use function `send_sms(to, body)`.
- Handles errors gracefully.

---

## 🛠️ Requirements
- Python 3.7+
- Twilio account with **WhatsApp Sandbox** enabled.
- Installed dependencies from `requirements.txt`

```bash
pip install twilio
```

---

## ⚙️ Setup

1. Clone this repository or copy the script.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your Twilio credentials in the script:
   ```python
   account_sid = "YOUR_TWILIO_ACCOUNT_SID"
   auth_token = "YOUR_TWILIO_AUTH_TOKEN"
   ```
4. Replace `from_` with your **Twilio WhatsApp number**:
   ```python
   from_="whatsapp:+14155238886"
   ```
   (The default Twilio Sandbox number is usually `+14155238886`.)

---

## ▶️ Usage
Run the script:

```bash
python send_whatsapp.py
```

It will ask:
```
Enter your name:
Enter your WhatsApp number:
Enter your message:
```

✅ Example:
```
Enter your name: Arpit
Enter your WhatsApp number: +919876543210
Enter your message: Hello from Twilio WhatsApp!
```

Output:
```
Message sent: SMxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 📌 Notes
- Make sure the recipient number has joined the **Twilio Sandbox** by sending `join <code>` to the sandbox number.
- Phone numbers must include the country code (e.g., `+91` for India).
- Twilio trial accounts can only send messages to verified numbers unless upgraded.

---

## 📄 License
This project is licensed under the MIT License.
