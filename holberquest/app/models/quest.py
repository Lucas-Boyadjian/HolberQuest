from app import db

class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255))
    reponses = db.Column(db.PickleType)  # ou JSON si tu veux
    bonne_reponse = db.Column(db.String(255))
    difficulte = db.Column(db.String(50))
    xp_gagne = db.Column(db.Integer)
    xp_perdu = db.Column(db.Integer)
    # La relation "combats" est déjà créée via backref dans Combat
