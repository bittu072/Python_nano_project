#this program will send a text message to provided mobile phone number


from twilio.rest import TwilioRestClient

account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # Your Account SID from www.twilio.com/console
auth_token  = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Your Auth Token from www.twilio.com/console

#to get account_sid and auth_token login to twilio.com

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="this is twilio",
    to="+1xxxxxxxxxx",    # Replace with your phone number, if not in usa replace +1 also
    from_="+1xxxxxxxxxx") # Replace with your Twilio number

print(message.sid)
