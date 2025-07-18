from flask import Blueprint, request, jsonify
from models.player import Player

player_bp = Blueprint('player', __name__)

@player_bp.route('/players', methods=['POST'])
def create_player():
    data = request.json
    username = data.get('username')
    avatar = data.get('avatar')
    if not username or not avatar:
        return jsonify({'error': 'Username and avatar are required'}), 400
    player = Player(username=username, avatar=avatar)
    player.save()
    return jsonify({'id': player.id, 'username': player.username, 'avatar': player.avatar}), 201

@player_bp.route('/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = Player.get_by_id(player_id)
    if player is None:
        return jsonify({'error': 'Player not found'}), 404
    return jsonify({
        'id': player.id,
        'username': player.username,
        'avatar': player.avatar,
        'level': player.level,
        'xp': player.xp
    })

@player_bp.route('/players/<int:player_id>/validate_challenge', methods=['POST'])
def validate_challenge(player_id):
    data = request.json
    challenge_result = data.get('result')
    if challenge_result is None:
        return jsonify({'error': 'Challenge result is required'}), 400
    player = Player.get_by_id(player_id)
    if player is None:
        return jsonify({'error': 'Player not found'}), 404
    if challenge_result:  # Assuming True means success
        player.gain_xp(10)  # Example XP gain
        return jsonify({'message': 'Challenge validated', 'xp': player.xp}), 200
    return jsonify({'message': 'Challenge failed'}), 400