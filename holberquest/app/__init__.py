from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()  # Charge le .env

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SLACK_BOT_TOKEN"] = os.getenv("SLACK_BOT_TOKEN")
app.config["SLACK_SIGNING_SECRET"] = os.getenv("SLACK_SIGNING_SECRET")
db = SQLAlchemy(app)
