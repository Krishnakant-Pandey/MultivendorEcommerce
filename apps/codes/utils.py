import os 
from twilio.rest import Client

account_sid = 'PlaceHolder' #The Twilio Api Account_Sid will come here
auth_token = 'PlaceHolder' # The Twilio Api Token will come here
client = Client(account_sid,auth_token)

def send_sms(user_code, phone_number):
    message = client.messages.create(
        body = f'Hi! Your user and verification code is {user_code}',
        from_='+15032785568',
        to=f'+91{phone_number}'
    )

    print(message.sid)