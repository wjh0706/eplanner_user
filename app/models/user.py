from .. import db

class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    profile_picture = db.Column(db.String(300))  # Assuming you store image URLs or paths
