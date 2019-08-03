from app import db


class Comments(db.Model):

    __tablename__ = "comments"

    uid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    # pub_date = 
    # username
    # email

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return '<title {}>'.format(self.body)