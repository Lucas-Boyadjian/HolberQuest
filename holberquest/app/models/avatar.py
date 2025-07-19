<<<<<<< HEAD
from app import db

class Avatar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    options = db.Column(db.JSON)
=======
from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User


class Avatar:
    pass


avatar_bp = Blueprint('avatar', __name__)

@avatar_bp.route('/avatar/<int:user_id>', methods=['PUT'])
def update_avatar(user_id):
    data = request.json
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user.avatar = data.get('avatar')
    db.session.commit()
    return jsonify({'message': 'Avatar updated', 'avatar': user.avatar}), 200
>>>>>>> origin/Dev3
