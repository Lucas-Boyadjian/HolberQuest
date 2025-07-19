import re
from flask import Blueprint, request, jsonify, render_template
from app import db
from app.models.user import User
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session

SECRET_KEY = "un_secret_pour_la_session"
auth_bp = Blueprint('auth', __name__)

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

@auth_bp.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

@auth_bp.route('/register', methods=['POST'])
def register():
    if request.is_json:
        data = request.get_json()
        is_api = True
    else:
        data = request.form
        is_api = False

    # Vérifie la présence du mot de passe
    if 'password' not in data or not data['password']:
        if is_api:
            return jsonify({'error': 'Mot de passe requis'}), 400
        else:
            return render_template('create_avatar.html', error="Mot de passe requis"), 400
    # Vérifie la présence de l'email
    if 'email' not in data or not data['email']:
        if is_api:
            return jsonify({'error': 'Email requis'}), 400
        else:
            return render_template('create_avatar.html', error="Email requis"), 400
    # Vérifie la regex
    if not re.match(EMAIL_REGEX, data['email']):
        if is_api:
            return jsonify({'error': 'Email invalide'}), 400
        else:
            return render_template('create_avatar.html', error="Email invalide"), 400
    # Vérifie l'unicité
    if User.query.filter_by(email=data['email']).first():
        if is_api:
            return jsonify({'error': 'Email already exists'}), 409
        else:
            return render_template('create_avatar.html', error="Email déjà utilisé"), 409
    # Vérifie la présence du pseudo
    if 'pseudo' not in data or not data['pseudo']:
        if is_api:
            return jsonify({'error': 'Pseudo requis'}), 400
        else:
            return render_template('create_avatar.html', error="Pseudo requis"), 400
    if User.query.filter_by(pseudo=data['pseudo']).first():
        if is_api:
            return jsonify({'error': 'Pseudo already exists'}), 409
        else:
            return render_template('create_avatar.html', error="Pseudo déjà utilisé"), 409

    user = User(
        pseudo=data['pseudo'],
        email=data['email'],
        avatar=data.get('avatar'),
        cohorte=data.get('cohorte'),
        campus=data.get('campus'),
        password_hash=generate_password_hash(data['password'])
    )
    db.session.add(user)
    db.session.commit()
    user.avatar = f"https://api.dicebear.com/7.x/bottts/svg?seed={user.id}"
    db.session.commit()

    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, SECRET_KEY, algorithm='HS256')

    if is_api:
        return jsonify({'message': 'User created', 'id': user.id, 'token': token}), 201
    else:
        return redirect('/login')


@auth_bp.route('/login', methods=['POST'])
def login():
    # Détecte si la requête est JSON
    if request.is_json:
        data = request.get_json()
        is_api = True
    else:
        data = request.form
        is_api = False

    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        if is_api:
            return jsonify({'error': 'Email et mot de passe requis'}), 400
        else:
            return render_template('login.html', error="Email et mot de passe requis"), 400

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        session['user_id'] = user.id  # <-- AJOUTE CETTE LIGNE
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, SECRET_KEY, algorithm='HS256')
        if is_api:
            return jsonify({'message': 'Login successful', 'id': user.id, 'token': token}), 200
        else:
            # Redirige vers le profil ou une autre page
            return render_template('profile.html', pseudo=user.pseudo, avatar=user.avatar)
    else:
        if is_api:
            return jsonify({'error': 'Identifiants invalides'}), 401
        else:
            return render_template('login.html', error="Identifiants invalides"), 401