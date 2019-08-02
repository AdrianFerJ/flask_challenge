from flask import Flask, request, render_template, jsonify
from flask_restful import reqparse, abort, Api, Resource

# Initiate app
app = Flask(__name__)
api = Api(app)

# set config
app.config.from_object('project.config.DevelopmentConfig')

# Temporary data
COMMENTS = {
    'cm1': {'title': 'First comment', 'text' : 'first text'},
    'cm2': {'title': '2nd comment', 'text' : 'not much text'},
    'cm3': {'title': 'No title?', 'text': '???'},
}

parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('text', type=str)

class CommentsList(Resource):

    def get(self):
        """ Get a list of all existing comments"""
        response_object = {
            'status': 'success',
            'message': f'List of comments',
            'data': COMMENTS
        }
        return response_object, 200

    def post(self):
        """ Add a new comment"""
        args = parser.parse_args(strict=True)
        # post_data = request.get_json()
        # title = post_data.get('title')
        # text = post_data.get('text')

        cm_id = int(max(COMMENTS.keys()).lstrip('cm')) + 1
        cm_id = 'cm%i' % cm_id

        COMMENTS[cm_id] = {'title': args['title'], 'text' : args['text']}

        response_object = {
            'status': 'success',
            'message': f'Comment {cm_id} was added!',
            'data': COMMENTS[cm_id]
        }
        return response_object, 201

# Add routing
api.add_resource(CommentsList, '/')


if __name__ == '__main__':
    app.run(debug=True)