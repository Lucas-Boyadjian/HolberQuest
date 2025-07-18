from app import app, db
from app.models.user import User
from app.models.avatar import Avatar
from app.models.quest import Quest
from app.models.combat import Combat

with app.app_context():
    db.create_all()
    print("Base de données créée !")