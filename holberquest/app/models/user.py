#!/usr/bin/env python3

from app import db

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pseudo = db.Column(db.String(80), unique=True, nullable=False)
    avatar = db.Column(db.String(255))
    xp = db.Column(db.Integer, default=0)
    niveau = db.Column(db.Integer, default=1)
    cohorte = db.Column(db.String(80))
    campus = db.Column(db.String(80))

    combats = db.relationship('Combat', foreign_keys='Combat.user_id', backref='joueur', lazy=True)
    combats_adversaire = db.relationship('Combat', foreign_keys='Combat.adversaire_id', backref='adversaire_obj', lazy=True)
    # Si tu veux lier les quêtes auxquelles le user a participé, il faut une table d'association ou un modèle "UserQuest"