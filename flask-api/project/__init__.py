
import os
from flask import Flask, jsonify
from flask_restful import Resource, Api


# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)
# app.config.from_object('project.config.DevelopmentConfig')

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