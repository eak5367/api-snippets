# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACdc5f132a3c49700934481addd5ce1659"
auth_token  = "{{ auth_token }}"
client = TwilioRestClient(account_sid, auth_token)

number = client.phone_numbers.update("PN2a0747eba6abf96b7e3c3ff0b4530f6e", voice_url="http://demo.twilio.com/docs/voice.xml",
    sms_url="http://demo.twilio.com/docs/sms.xml")
print number.voice_url