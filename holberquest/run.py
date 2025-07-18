from app.slack_bot.bot import slack_bot
from flask import Flask

app = Flask(__name__)
app.register_blueprint(slack_bot)
