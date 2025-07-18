from flask import Blueprint, request, jsonify
from ..models.quest import Quest

quest_bp = Blueprint('quest', __name__)

@quest_bp.route('/quests', methods=['GET'])
def get_quests():
    quests = Quest.get_all_quests()
    return jsonify(quests), 200

@quest_bp.route('/quests/<int:quest_id>', methods=['GET'])
def get_quest(quest_id):
    quest = Quest.get_quest_by_id(quest_id)
    if quest:
        return jsonify(quest), 200
    return jsonify({'error': 'Quest not found'}), 404

@quest_bp.route('/quests/submit', methods=['POST'])
def submit_answer():
    data = request.json
    quest_id = data.get('quest_id')
    answer = data.get('answer')
    
    quest = Quest.get_quest_by_id(quest_id)
    if quest:
        if quest['answer'] == answer:
            return jsonify({'message': 'Correct answer!'}), 200
        else:
            return jsonify({'message': 'Incorrect answer!'}), 400
    return jsonify({'error': 'Quest not found'}), 404