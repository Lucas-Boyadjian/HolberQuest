from app import db

class Avatar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    options = db.Column(db.JSON)