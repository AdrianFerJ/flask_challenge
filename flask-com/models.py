from app import db
from datetime import datetime


class Comments(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String, nullable=False)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, username, text, email):
        self.username = username
        self.text = text
        self.email = email

    def __repr__(self):
        return f'<comment {self.id} by {self.username}>'