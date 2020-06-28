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
    account_sid = "AC086a5ea5f6b1f60d1620b403b0773b9e"
    auth_token = "049ec69bcb74eb573f7710ec65fc2039"
    client = Client(account_sid, auth_token)
    try:
        for i in range(1,31):
            """if i>10:
                break"""
            l = i*3
            message = client.messages.create(
                to="{}".format(number),
                from_="whatsapp:+14155238886",
                body='{}\n----------------\n{}\n------------------'.format(results[l-3],results[l-2]))
            time.sleep(0.25)
            message = client.messages.create(
                to="{}".format(number),
                from_="whatsapp:+14155238886",
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