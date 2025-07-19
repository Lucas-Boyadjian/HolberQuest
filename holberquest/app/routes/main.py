from flask import Blueprint, render_template, request, redirect, url_for, session

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('login.html')

@main_bp.route('/profile')
def profile():
    pseudo = session.get('pseudo', 'Stephane')
    avatar = session.get('avatar', 'hypo.png')
    # Passe ces variables au template
    return render_template('profile.html', pseudo=pseudo, avatar=avatar)

@main_bp.route('/leaderboard')
def leaderboard():
    users = [
        {'pseudo': 'Alice', 'niveau': 15, 'xp': 1200, 'avatar': None},
        {'pseudo': 'Bob', 'niveau': 13, 'xp': 950, 'avatar': None},
        {'pseudo': 'Stephane', 'niveau': 12, 'xp': 750, 'avatar': None},
        {'pseudo': 'David', 'niveau': 11, 'xp': 600, 'avatar': None},
        {'pseudo': 'Laura', 'niveau': 10, 'xp': 500, 'avatar': None},
        {'pseudo': 'Michael', 'niveau': 9, 'xp': 400, 'avatar': None},
        {'pseudo': 'Sarah', 'niveau': 8, 'xp': 300, 'avatar': None},
        {'pseudo': 'Chris', 'niveau': 7, 'xp': 250, 'avatar': None},
        {'pseudo': 'Jessica', 'niveau': 6, 'xp': 200, 'avatar': None},
        {'pseudo': 'Daniel', 'niveau': 5, 'xp': 150, 'avatar': None},
        {'pseudo': 'Emma', 'niveau': 4, 'xp': 100, 'avatar': None},
        {'pseudo': 'Oliver', 'niveau': 4, 'xp': 100, 'avatar': None},
        {'pseudo': 'Sophia', 'niveau': 3, 'xp': 80, 'avatar': None},
        {'pseudo': 'James', 'niveau': 3, 'xp': 80, 'avatar': None},
        {'pseudo': 'Charlotte', 'niveau': 2, 'xp': 60, 'avatar': None},
        {'pseudo': 'Elijah', 'niveau': 2, 'xp': 60, 'avatar': None},
        {'pseudo': 'Amelia', 'niveau': 2, 'xp': 50, 'avatar': None},
        {'pseudo': 'Benjamin', 'niveau': 1, 'xp': 30, 'avatar': None},
        {'pseudo': 'Isabella', 'niveau': 1, 'xp': 30, 'avatar': None},
        {'pseudo': 'Zoe', 'niveau': 2, 'xp': 120, 'avatar': None},
    ]
    return render_template('leaderboard.html', users=users)

@main_bp.route('/login')
def login():
    return render_template('login.html')

@main_bp.route('/combat')
def combat():
    from app.models.quest import Quest
    from app import db
    quest = Quest.query.order_by(db.func.random()).first()
    if not quest:
        return "Aucune question disponible", 404
    return redirect(url_for('quest.view_quest', quest_id=quest.id))

@main_bp.route('/create_avatar', methods=['GET', 'POST'])
def create_avatar():
    if request.method == 'POST':
        pseudo = request.form.get('pseudo')
        avatar = request.form.get('selectedAvatar')
        session['pseudo'] = pseudo
        session['avatar'] = avatar
        return redirect(url_for('main.profile'))
    return render_template('create_avatar.html')

