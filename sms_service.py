
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXX'
auth_token = 'acXXXXXXXXX'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12058272450',
                     to='+17324047720'
                 )

print(message.sid)

#import os

#from dotenv import load_dotenv
#from twilio.rest import Client

#load_dotenv()

#TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "OOPS, please specify env var called 'TWILIO_ACCOUNT_SID'")
#TWILIO_AUTH_TOKEN  = os.environ.get("TWILIO_AUTH_TOKEN", "OOPS, please specify env var called 'TWILIO_AUTH_TOKEN'")
#SENDER_SMS  = os.environ.get("SENDER_SMS", "OOPS, please specify env var called 'SENDER_SMS'")
#RECIPIENT_SMS  = os.environ.get("RECIPIENT_SMS", "OOPS, please specify env var called 'RECIPIENT_SMS'")

# AUTHENTICATE

#client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# COMPILE REQUEST PARAMETERS (PREPARE THE MESSAGE)

#content = "Hello, this is a message from your personal notification service. TODO: customize me!"

# ISSUE REQUEST (SEND SMS)

#message = client.messages.create(to=RECIPIENT_SMS, from_=SENDER_SMS, body=content)

# PARSE RESPONSE

#print("----------------------")
#print("SMS")
#print("----------------------")
#print("RESPONSE: ", type(message))
#print("FROM:", message.from_)
#print("TO:", message.to)
#print("BODY:", message.body)
#print("PROPERTIES:")
#print(message._properties)