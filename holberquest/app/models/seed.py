from app import db
from app.models.quest import Quest
import json

def seed_quest():
    quests = [
        Quest(
            question="Quel est le langage principal de Flask ?",
            reponses=["JavaScript", "Python", "PHP", "Ruby"],
            bonne_reponse="Python",
            difficulte="facile",
            xp_gagne=10,
            xp_perdu=2
        ),
        Quest(
            question="Quelle commande initialise un projet Git ?",
            reponses=["git start", "git init", "git push", "git clone"],
            bonne_reponse="git init",
            difficulte="facile",
            xp_gagne=10,
            xp_perdu=2
        )
    ]

    db.session.bulk_save_objects(quests)
    db.session.commit()
    print("Base de Quests insérée.")
