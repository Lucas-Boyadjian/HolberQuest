from app.slack_bot.bot import slack_bot
from flask import Flask
from app import app
from app.routes.main import main_bp
from app.routes.combat import combat_bp
from app.routes.auth import auth_bp
from app.scheduler import scheduler  # Ajoute cette ligne pour démarrer le scheduler


app.register_blueprint(slack_bot)
app.register_blueprint(main_bp)
app.register_blueprint(combat_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)