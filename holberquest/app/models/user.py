from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pseudo = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    avatar = db.Column(db.String(255))
    xp = db.Column(db.Integer, default=0)
    niveau = db.Column(db.Integer, default=1)
    cohorte = db.Column(db.String(80))
    campus = db.Column(db.String(80))
    slack_id = db.Column(db.String(50), unique=True)
    combats = db.relationship('Combat', backref='joueur', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)