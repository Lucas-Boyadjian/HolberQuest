from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    avatar = Column(String(100), nullable=False)
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)

    def __init__(self, username, avatar):
        self.username = username
        self.avatar = avatar

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'avatar': self.avatar,
            'level': self.level,
            'experience': self.experience
        }

    @classmethod
    def create_player(cls, username, avatar):
        new_player = cls(username=username, avatar=avatar)
        db.session.add(new_player)
        db.session.commit()
        return new_player

    @classmethod
    def get_player(cls, player_id):
        return cls.query.get(player_id)

    @classmethod
    def get_all_players(cls):
        return cls.query.all()