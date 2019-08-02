
import os
from datetime import datetime
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy 


# instantiate the app
app = Flask(__name__)

api = Api(app)

# Set up app config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# Initiate DB
db = SQLAlchemy(app)

# model
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(62), nullable=False)
    text = db.Column(db.Text(128), nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    username = db.Column(db.String(62), nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, username, email):
        self.username = username
        self.email = email


# Add comments
# from project.api.comments import CommentsList
# api.add_resource(CommentsList, '/comments')


class UsersPing(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'pong!'
    }

api.add_resource(UsersPing, '/ping')