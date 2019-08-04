from app import db


class Comments(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String, nullable=False)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    pub_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, title, text):
        self.username = title
        self.text = text

    def __repr__(self):
        return '<comment {}>'.format(self.id)