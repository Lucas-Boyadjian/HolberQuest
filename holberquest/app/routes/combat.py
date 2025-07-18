from flask import Blueprint, request, jsonify
from app import db
from app.models.combat import Combat

combat_bp = Blueprint('combat', __name__)

@combat_bp.route('/combat', methods=['POST'])
def create_combat():
    data = request.json
    combat = Combat(
        user_id=data['user_id'],
        adversaire_id=data.get('adversaire_id'),
        quest_id=data['quest_id'],
        resultat=data['resultat']
    )
    db.session.add(combat)
    db.session.commit()
    return jsonify({'message': 'Combat saved', 'combat_id': combat.id}), 201