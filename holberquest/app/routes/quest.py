from flask import Blueprint, jsonify, request
from app.models.quest import Quest
from app import db

quest_bp = Blueprint('quest', __name__)


@quest_bp.route('/quest/<int:quest_id>', methods=['GET'])
def get_quest(quest_id):
    quest = Quest.query.get(quest_id)
    if not quest:
        return jsonify({'message': 'Quest not found'}), 404
    return jsonify({
        'id': quest.id,
        'question': quest.question,
        'reponses': quest.reponses,
        'difficulte': quest.difficulte,
        'xp_gagne': quest.xp_gagne,
        'xp_perdu': quest.xp_perdu
    }), 200

# Endpoint POST pour créer une quête avec validation
@quest_bp.route('/quest', methods=['POST'])
def create_quest():
    data = request.json
    if not data:
        return jsonify({'error': 'Aucune donnée reçue'}), 400
    required_fields = ['question', 'reponses', 'bonne_reponse', 'difficulte', 'xp_gagne', 'xp_perdu']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Champ requis manquant: {field}'}), 400
    try:
        quest = Quest(
            question=data['question'],
            reponses=data['reponses'],
            bonne_reponse=data['bonne_reponse'],
            difficulte=data['difficulte'],
            xp_gagne=int(data['xp_gagne']),
            xp_perdu=int(data['xp_perdu'])
        )
        db.session.add(quest)
        db.session.commit()
        return jsonify({'message': 'Quête créée', 'id': quest.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@quest_bp.route('/quests', methods=['GET'])
def list_quests():
    quests = Quest.query.all()
    data = [{
        'id': q.id,
        'question': q.question,
        'reponses': q.reponses,
        'difficulte': q.difficulte,
        'xp_gagne': q.xp_gagne,
        'xp_perdu': q.xp_perdu
    } for q in quests]
    return jsonify(data), 200

@quest_bp.route('/quest/daily', methods=['GET'])
def daily_quest():
    # Sélectionne une quête aléatoire (ou selon une logique de rotation)
    quest = Quest.query.order_by(db.func.random()).first()
    if not quest:
        return jsonify({'message': 'Aucune quête disponible'}), 404
    return jsonify({
        'id': quest.id,
        'question': quest.question,
        'reponses': quest.reponses,
        'difficulte': quest.difficulte,
        'xp_gagne': quest.xp_gagne,
        'xp_perdu': quest.xp_perdu
    }), 200