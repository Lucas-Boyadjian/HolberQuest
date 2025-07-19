# Webhook listener

import os
import time
import hmac
import hashlib
from flask import Blueprint, request, jsonify, abort, current_app as app
from app.utils.helpers import start_combat_for_user  # À créer

slack_bot = Blueprint('slack_bot', __name__)

SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")



def verify_slack_request(req):
    from flask import current_app
    slack_signing_secret = current_app.config["SLACK_SIGNING_SECRET"]
    
    timestamp = req.headers.get('X-Slack-Request-Timestamp')
    slack_signature = req.headers.get('X-Slack-Signature')
    
    if abs(time.time() - int(timestamp)) > 60 * 5:
        return False

    sig_basestring = f"v0:{timestamp}:{req.get_data(as_text=True)}"
    my_signature = 'v0=' + hmac.new(
       
        sig_basestring.encode(), slack_signing_secret.encode(),
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(my_signature, slack_signature)


@slack_bot.route('/slack/events', methods=['POST'])
def slack_events():
    data = request.json

    # 1. Verification initiale Slack (connexion du bot)
    if data.get('type') == 'url_verification':
        return jsonify({'challenge': data.get('challenge')})

    # Vérification de sécurité Slack (pour les autres requêtes)
    if not verify_slack_request(request):
        abort(403)

    # 2. Traitement des événements
    event = data.get('event', {})
    event_type = event.get('type')

    if event_type == 'app_mention':
        user_id = event.get('user')
        text = event.get('text').lower()

        if 'start' in text:
            # Appelle ta logique de combat ici
            start_combat_for_user(user_id)  # à implémenter
            return jsonify({
                'text': f"<@{user_id}> tu viens de déclencher une quête ! Prépare-toi à combattre !"
            })

    return '', 200
