#!/usr/bin/env python3

from app import db

class Quest(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    reponses = db.Column(db.JSON, nullable=False)  # Liste de réponses possibles
    bonne_reponse = db.Column(db.String(255), nullable=False)
    difficulte = db.Column(db.String(50))
    xp_gagne = db.Column(db.Integer, default=10)
    xp_perdu = db.Column(db.Integer, default=0)

class QCM:
    pass
