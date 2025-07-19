import re
from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User
import jwt
import datetime

SECRET_KEY = "un_secret_pour_la_session"
auth_bp = Blueprint('auth', __name__)

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    # Vérifie la présence de l'email
    if 'email' not in data or not data['email']:
        return jsonify({'error': 'Email requis'}), 400
    # Vérifie la regex
    if not re.match(EMAIL_REGEX, data['email']):
        return jsonify({'error': 'Email invalide'}), 400
    # Vérifie l'unicité
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already exists'}), 409
    # Vérifie la présence du pseudo
    if 'pseudo' not in data or not data['pseudo']:
        return jsonify({'error': 'Pseudo requis'}), 400
    if User.query.filter_by(pseudo=data['pseudo']).first():
        return jsonify({'error': 'Pseudo already exists'}), 409

    user = User(
        pseudo=data['pseudo'],
        email=data['email'],
        avatar=data.get('avatar'),
        cohorte=data.get('cohorte'),
        campus=data.get('campus')
    )
    db.session.add(user)
    db.session.commit()
    user.avatar = f"https://api.dicebear.com/7.x/bottts/svg?seed={user.id}"
    db.session.commit()

    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, SECRET_KEY, algorithm='HS256')

    return jsonify({'message': 'User created', 'id': user.id, 'token': token}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'pseudo' not in data:
        return jsonify({'error': 'Pseudo requis'}), 400
    user = User.query.filter_by(pseudo=data['pseudo']).first()
    if user:
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, SECRET_KEY, algorithm='HS256')
        return jsonify({'message': 'Login successful', 'id': user.id, 'token': token}), 200
    return jsonify({'error': 'Utilisateur non trouvé'}), 404