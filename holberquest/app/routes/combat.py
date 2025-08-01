from flask import Blueprint, request, jsonify
from app import db
from app.models.combat import Combat
from app.models.user import User  # Import User model
from app.utils.helpers import gain_xp
from flask import session

combat_bp = Blueprint('combat', __name__)

@combat_bp.route('/combat', methods=['POST'])
def create_combat():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'Utilisateur non connecté'}), 401
    data = request.json
    # Validation des champs requis (sans user_id)
    required_fields = ['quest_id', 'resultat']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Champ requis manquant: {field}'}), 400
    try:
        combat = Combat(
            user_id=user_id,
            quest_id=data['quest_id'],
            resultat=data['resultat'],
            date=data.get('date'),
            etat="en_cours"
        )
        db.session.add(combat)
        user = User.query.get(user_id)  # <-- Utilise l'id de session ici
        if user and data['resultat'] == 'win':
            gain_xp(user, 20)
        db.session.commit()
        return jsonify({'message': 'Combat enregistré', 'combat_id': combat.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@combat_bp.route('/combat/history/<int:user_id>', methods=['GET'])
def combat_history(user_id):
    combats = Combat.query.filter_by(user_id=user_id).all()
    history = [{
        'id': c.id,
        'quest_id': c.quest_id,
        'resultat': c.resultat,
        'date': c.date
    } for c in combats]
    return jsonify(history), 200