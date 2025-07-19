from app.slack_bot.bot import slack_bot
from flask import Flask
from app import app


app.register_blueprint(slack_bot)

if __name__ == "__main__":
    app.run(debug=True)