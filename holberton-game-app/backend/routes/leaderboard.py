from flask import Blueprint, jsonify
from ..models.player import Player

leaderboard_bp = Blueprint('leaderboard', __name__)

@leaderboard_bp.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    players = Player.query.order_by(Player.experience.desc()).limit(10).all()
    leaderboard = [{'username': player.username, 'level': player.level, 'experience': player.experience} for player in players]
    return jsonify(leaderboard)