from flask import Blueprint, request, jsonify
import json
from app import db
from app.models.quest import Quest
from app.utils.helpers import resolve_qcm_response

slack_interactions = Blueprint('slack_interactions', __name__)

@slack_interactions.route('/slack/interactions', methods=['POST'])
def slack_actions():
    payload = json.loads(request.form['payload'])
    user_id = payload['user']['id']
    action = payload['actions'][0]
    value = action['value']  # Format : quest_id|user_choice

    quest_id, user_choice = map(int, value.split('|'))
    resolve_qcm_response(user_id, quest_id, user_choice)

    return jsonify({
        'text': f"<@{user_id}> tu as choisi la réponse {user_choice}. Résultat en cours..."
    })
