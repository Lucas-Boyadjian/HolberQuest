from flask import Flask
from flask_cors import CORS
from backend.routes.player import player_routes
from backend.routes.quest import quest_routes
from backend.routes.leaderboard import leaderboard_routes
import sqlite3

app = Flask(__name__)
CORS(app)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('backend/database/db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

# Register routes
app.register_blueprint(player_routes)
app.register_blueprint(quest_routes)
app.register_blueprint(leaderboard_routes)

@app.route('/')
def home():
    return "Welcome to the Holberton Game API!"

if __name__ == '__main__':
    app.run(debug=True)