from app import db
from app.models.quest import QCM
import json

def seed_qcm():
    qcms = [
        QCM(
            question="Quel est le langage principal de Flask ?",
            choices=json.dumps(["JavaScript", "Python", "PHP", "Ruby"]),
            correct_index=1
        ),
        QCM(
            question="Quelle commande initialise un projet Git ?",
            choices=json.dumps(["git start", "git init", "git push", "git clone"]),
            correct_index=1
        )
    ]

    db.session.bulk_save_objects(qcms)
    db.session.commit()
    print("Base de QCM insérée.")
