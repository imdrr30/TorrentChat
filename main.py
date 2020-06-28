from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import torrent
from twilio.rest import Client
import time

app = Flask(__name__)




@app.route("/")
def hello():
    return "Service is Active"

@app.route("/sms", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')
    number = request.form.get('From')
    results = torrent.getdata(msg)
    account_sid = "YOUR_ACCOUNT_SID_HERE"
    auth_token = "YOUR_AUTH_TOKEN_HERE"
    client = Client(account_sid, auth_token)
    try:
        for i in range(1,31):
            """if i>10:
                break"""
            l = i*3
            sandnum="whatsapp:YOUR_SANDBOX_NUMBER_HERE"
            message = client.messages.create(
                to="{}".format(number),
                from_=sandnum,
                body='{}\n----------------\n{}\n------------------'.format(results[l-3],results[l-2]))
            time.sleep(0.25)
            message = client.messages.create(
                to="{}".format(number),
                from_=sandnum,
                body='{}'.format(results[l - 1]))
            time.sleep(0.25)
    except:
        pass

    resp = MessagingResponse()
    if results == []:
        resp.message('No matching results found.')
    else:
        resp.message('End of results(1-5)')
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
