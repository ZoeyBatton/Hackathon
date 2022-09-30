from twilio.rest import Client
account_sid = 'AC10e31a7cfcd37aee8370d2bc09468b25'
account_token = '9f588b3eda127e946a95df97e62ef3da'

client = Client(account_sid, account_token)

message = client.messages.create(
    messaging_service_sid = 'MGdb54e56bf0ab026edbd4181ec8f08a0c',
    body = "This is working yay",
    to = '+13303014724'
    )

print(message.sid)