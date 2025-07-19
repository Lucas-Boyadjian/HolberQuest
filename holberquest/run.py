from app.slack_bot.bot import slack_bot
from flask import Flask, session
from app import app
from app.routes.main import main_bp
from app.routes.combat import combat_bp
from app.routes.auth import auth_bp
from app.routes.quest import quest_bp
from app.scheduler import scheduler  # Ajoute cette ligne pour démarrer le scheduler
from app.scheduler import send_daily_question  # Import the missing function

app.secret_key = "un_secret_pour_la_session"

app.register_blueprint(slack_bot)
app.register_blueprint(main_bp)
app.register_blueprint(combat_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(quest_bp)

if __name__ == "__main__":
    app.run(debug=True)