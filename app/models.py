from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=True)
    password_hash = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)