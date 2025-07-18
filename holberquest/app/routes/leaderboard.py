from flask import Blueprint, jsonify
from app.models.user import User

leaderboard_bp = Blueprint('leaderboard', __name__)

@leaderboard_bp.route('/leaderboard', methods=['GET'])
def leaderboard():
    users = User.query.order_by(User.xp.desc()).limit(10).all()
    data = [{'pseudo': u.pseudo, 'xp': u.xp, 'niveau': u.niveau} for u in users]
    return jsonify(data), 200