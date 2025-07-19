from app import db

class Combat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    adversaire_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    quest_id = db.Column(db.Integer, db.ForeignKey('quest.id'))
    resultat = db.Column(db.String(50))
    date = db.Column(db.DateTime)

    user = db.relationship('User', foreign_keys=[user_id])
    adversaire = db.relationship('User', foreign_keys=[adversaire_id])
    quest = db.relationship('Quest', backref='combats')