from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACbca5b291a65a7cb029f33bf95dc56249"
auth_token  = "bc03939c3ce56fd8f83d76269c4ee9ea"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Comm check, comm check",
    to="+15135496685",    # Replace with your phone number
    from_="+15134297741") # Replace with your Twilio number
print message.sid