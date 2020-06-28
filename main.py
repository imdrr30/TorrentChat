from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import torrent

results = ['empty']
app = Flask(__name__)


@app.route("/")
def hello():
    return "Service is Active"

@app.route("/sms", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')
    res = ''
    res1 = ''
    if msg.isnumeric():
        if torrent.prev==[]:
            res='No torrent searchers were made before.'
        else:
            res = torrent.prev[(int(msg)*3)-1]
    else:
        results = torrent.getdata(msg)
        torrent.prev = results
        if results==[]:
            res='No results found'
        else:
            results1 = results[:45]
            results2 = results[45:]
            for i in range(0, len(results1)):
                if i % 3 == 0:
                    res += '*{}. {}*\n{}\n\n'.format((i // 3) + 1, results1[i], results1[i + 1][:-10])
            if len(results)>=45:
                for i in range(0, len(results2)):
                    if i % 3 == 0:
                        res1 += '*{}. {}*\n{}\n\n'.format((i // 3) + 16, results2[i], results2[i + 1][:-10])

    resp = MessagingResponse()
    resp.message(res)
    if res1!='':
        resp.message(res1)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)