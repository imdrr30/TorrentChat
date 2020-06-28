# TorrentChat
Get torrent search results via WhatsApp.
- ![Demo](https://github.com/revanrohith/TorrentChat/raw/master/demo.gif)
## Set it up
## Get Twilio Trail Account
- Sign up for Twilio
- Enable WhatsApp SandBox
- Register your number to your sandbox following the instructions on the site.
## Heroku Deployment
### Getting Account
In order work in backgroud we need to deploy in server.
- Get Heroku Free Dyno Account
- Install Heroku-CLI in your Machine
- In terminal or cmd enter:
- `heroku login`
- After Logging in
- Create an App.
- `heroku apps:create [NEW_APP_NAME]`
- Access that App
- `heroku git:remote -a YOUR_APP_NAME`
### Push it to server
- Go to the repo directoy.
```
git init
git add .
git commit -m "service"
git push heroku master
```
- Paste this in terminal or cmd to deploy.
### Changes in Twilio
- Go to Programmable SMS -> WhatsApp -> Sandbox.
- In Sandbox Configuration, Change `WHEN A MESSAGE COMES IN` parameter to `YOUR_APP_NAME.herokuapp.com/sms`
- Save it Twice.
## Enjoy Torrenting :)
