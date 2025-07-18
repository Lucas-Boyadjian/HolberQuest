from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from backend.routes.player import player_routes
from backend.routes.quest import quest_routes
from backend.routes.leaderboard import leaderboard_routes

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backend/database/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Register routes
app.register_blueprint(player_routes)
app.register_blueprint(quest_routes)
app.register_blueprint(leaderboard_routes)

@app.route('/')
def home():
    return "Welcome to the Holberton Game API!"

if __name__ == '__main__':
    app.run(debug=True)