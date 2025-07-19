# Utility functions

import os
import random
import requests
from app.models.quest import Quest
from app import db


SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_API_URL = "https://slack.com/api/chat.postMessage"

def send_message_to_user(user_id, text, blocks=None):
    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-type": "application/json"
    }
    payload = {
        "channel": user_id,
        "text": text,
    }
    if blocks:
        payload["blocks"] = blocks

    response = requests.post(SLACK_API_URL, json=payload, headers=headers)
    return response.json()


def start_combat_for_user(user_id):
    # Sélectionne un QCM aléatoire depuis la base
    qcm = QCM.query.order_by(db.func.random()).first()
    if not qcm:
        send_message_to_user(user_id, "Aucune question QCM disponible pour le moment.")
        return

    # Crée les blocs Slack avec boutons pour chaque réponse
    blocks = [
        {"type": "section", "text": {"type": "mrkdwn", "text": f"*⚔️ Combat :* {qcm.question}"}},
        {"type": "actions", "elements": []}
    ]

    for idx, choice in enumerate(qcm.choices):
        blocks[1]["elements"].append({
            "type": "button",
            "text": {"type": "plain_text", "text": choice},
            "value": f"{qcm.id}|{idx}",  # ex: 5|2 (id QCM 5, choix index 2)
            "action_id": "answer_qcm"
        })

    send_message_to_user(user_id, "Une quête commence !", blocks=blocks)

    # À ce stade, il faut que tu crées un handler pour les réponses (interactions Slack) avec l’action "answer_qcm"
def calculer_niveau(xp):
    # Exemple simple : 100 XP par niveau
    return xp // 100 + 1

def gain_xp(user, xp_gagne):
    user.xp += xp_gagne
    user.niveau = calculer_niveau(user.xp)

def get_user_rank(user):
    from app.models.user import User
    better_users = User.query.filter(User.xp > user.xp).count()
    return better_users + 1

def lose_xp(user, xp_perdu):
    user.xp = max(0, user.xp - xp_perdu)
    user.niveau = calculer_niveau(user.xp)
