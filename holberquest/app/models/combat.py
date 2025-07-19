from app import db

from app import db

class Combat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quest_id = db.Column(db.Integer, db.ForeignKey('quest.id'))
    resultat = db.Column(db.String(50))
    date = db.Column(db.DateTime)
    etat = db.Column(db.String(20), default="en_cours")
    quest = db.relationship('Quest', backref='combats')