
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXX'
auth_token = 'acXXXXXXXXXXXXXXXXXXXXX'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Don't forget sunblock today",
                     from_='+12058272450',
                     to='+XXXXXXXXXX'
                 )

print(message.sid)


#pip intall twilio
