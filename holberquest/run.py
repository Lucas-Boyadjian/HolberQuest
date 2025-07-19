from app.slack_bot.bot import slack_bot
from flask import Flask, session
from app import app

app.secret_key = "un_secret_pour_la_session"

if __name__ == "__main__":
    app.run(debug=True)