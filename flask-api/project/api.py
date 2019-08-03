from flask import Flask, request, render_template
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

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
        return COMMENTS

    def post(self):
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

api.add_resource(CommentsList, '/')


if __name__ == '__main__':
    app.run(debug=True)