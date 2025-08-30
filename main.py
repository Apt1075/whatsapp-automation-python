from twilio.rest import Client
from datetime import datetime, timedelta 
import time

account_sid = '' # Your Account SID
auth_token = '' # Your Auth Token
client = Client(account_sid, auth_token)


def send_sms(to, body):
    try:
        message = client.messages.create(
            to=f'whatsapp:{to}',
            from_='', # Your Twilio WhatsApp number with country code whatsapp:+123456789
            body=body
        )
        print(f"Message sent: {message.sid}")
    except Exception as e:
        print(f"Error sending message: {e}")

name = input("Enter your name: ")
phone_number = input("Enter your whatsapp number: ")
message_body = input(f"Enter your message: ")

send_sms(phone_number, message_body)
