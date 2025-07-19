# Utility functions

import os
import random
import requests
from app.models.quest import Quest  # Remplace QCM par Quest
from app import db
from flask import current_app
from app.utils.timer import start_timer


SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_API_URL = "https://slack.com/api/chat.postMessage"

# In-memory store for combat state per user (consider replacing with persistent storage in production)
combat_data = {}

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
    resp_json = response.json()
    if not resp_json.get("ok"):
        print(f"[Slack API Error] {resp_json}")
    return resp_json


def start_combat_for_user(user_id):
    # Vérifie si un combat est déjà en cours pour cet utilisateur
    if user_id in combat_data:
        send_message_to_user(user_id, "⚠️ Tu as déjà un combat en cours ! Termine-le avant d'en commencer un nouveau.")
        return

    # Sélectionne une Quest aléatoire depuis la base
    quest = Quest.query.order_by(db.func.random()).first()
    if not quest:
        send_message_to_user(user_id, "Aucune question QCM disponible pour le moment.")
        return

    # Crée les blocs Slack avec boutons pour chaque réponse
    blocks = [
        {"type": "section", "text": {"type": "mrkdwn", "text": f"*⚔️ Combat :* {quest.question}"}},
        {"type": "actions", "elements": []}
    ]

    for idx, choice in enumerate(quest.reponses):
        blocks[1]["elements"].append({
            "type": "button",
            "text": {"type": "plain_text", "text": choice},
            "value": f"{quest.id}|{idx}",
            "action_id": "answer_qcm"
        })

    send_message_to_user(user_id, "Une quête commence !", blocks=blocks)
    start_timer(user_id, quest.id)

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

def resolve_qcm_response(user_id, quest_id, user_choice):
    from app.models.user import User
    combat_data.pop(user_id, None)

    quest = Quest.query.get(quest_id)
    user = get_or_create_user(user_id)
    if not quest:
        return

    # Vérifie que l'index de réponse est valide
    if not isinstance(user_choice, int) or user_choice < 0 or user_choice >= len(quest.reponses):
        send_message_to_user(user_id, ":warning: Réponse invalide ou question expirée.")
        return

    # Trouve l'index de la bonne réponse
    try:
        correct_index = quest.reponses.index(quest.bonne_reponse)
    except ValueError:
        correct_index = -1

    if correct_index == user_choice:
        send_message_to_user(user_id, ":white_check_mark: Bonne réponse ! Tu gagnes de l'XP.")
        gain_xp(user, quest.xp_gagne)
    else:
        send_message_to_user(user_id, ":x: Mauvaise réponse ! Tu perds de l'XP.")
        lose_xp(user, quest.xp_perdu)
    from app import db
    db.session.commit()

def auto_fail_combat(user_id):
    from app.models.user import User
    combat_data.pop(user_id, None)
    user = get_or_create_user(user_id)
    # Optionnel: tu peux retrouver le dernier QCM pour l'user si besoin
    send_message_to_user(user_id, ":hourglass_flowing_sand: Temps écoulé ! Tu as perdu le combat.")
    if user:
        # Par défaut, perte de 5 XP si pas de QCM associé
        lose_xp(user, 5)
        from app import db
        db.session.commit()

def get_or_create_user(slack_id):
    from app.models.user import User
    user = User.query.filter_by(slack_id=slack_id).first()
    if not user:
        user = User(slack_id=slack_id, xp=0, niveau=1)
        db.session.add(user)
        db.session.commit()
    return user
