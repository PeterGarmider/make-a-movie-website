from twilio.rest import Client

account_sid = "AC97ccfffcaef30905e21917a13527bbb5"
auth_token = "7a379e4d3a16137186f67ccb8b19860f"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body = "This is a test SMS.",
    to = "16477857417",
    from_ = "16473602335")
print(message.sid)