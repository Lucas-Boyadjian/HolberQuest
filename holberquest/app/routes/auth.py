from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    existing_user = User.query.filter_by(pseudo=data['pseudo']).first()
    if existing_user:
        return jsonify({'error': 'Pseudo déjà utilisé'}), 400
    user = User(
        pseudo=data['pseudo'],
        avatar=data.get('avatar'),
        cohorte=data.get('cohorte'),
        campus=data.get('campus')
    )
    db.session.add(user)
    db.session.commit()
    user.avatar = f"https://api.dicebear.com/7.x/bottts/svg?seed={user.id}"
    db.session.commit()
    return jsonify({'message': 'User created', 'id': user.id}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(pseudo=data['pseudo']).first()
    if user:
        return jsonify({'message': 'Login successful', 'id': user.id}), 200
    return jsonify({'message': 'User not found'}), 404