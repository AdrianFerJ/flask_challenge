import os
from threading import Lock
from flask import Flask, render_template, session 
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

# get base directory where this file runs
basedir = os.path.abspath(os.path.dirname(__file__))

# App configuration
DATABASE = 'comments.db'
DEBUG = True
SECRET_KEY = 'ShhuperSecreto!'
USERNAME = 'admin'
PASSWORD = 'admin'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# database config
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Create App
app = Flask(__name__)
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)
# app.config['SECRET_KEY'] = SECRET_KEY
# app.config.from_object(__name__)

db = SQLAlchemy(app)

# import models
class Comments(db.Model):

    __tablename__ = "comments"

    uid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    # pub_date = 
    # username = db.Column(db.String(80), unique=True, nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return '<title {}>'.format(self.title)


# Enable async_mode in convination with "eventlet" or "gevent"
# Set this variable to "threading"
async_mode = None

# Websocket configuration
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()



@app.route('/')
def index():
    """ Endpoint to serve index.html """
    # entries = db.session.query(models.Comments)
    entries = db.session.query(Comments)

    # return render_template('index.html', async_mode=socketio.async_mode)
    return render_template('index.html', entries=entries)


@socketio.on('my_comments_event', namespace='/test')
def add_new_comments(message):
    """ Endpoint to create new comments and broadcast it to subscribers"""

    session['receive_count'] = session.get('receive_count', 0) + 1

    # Parse message
    # TODO add form data validation
    title = message['data']['title']
    text = message['data']['text']
    payload = title + ', ' + text

    # Add new comment to db
    # new_comment = models.Comments(title=title, text=text)
    new_comment = Comments(title=title, text=text)

    db.session.add(new_comment)
    db.session.commit()

    # Emit response
    emit('my_response',
         {'data': payload, 'count': session['receive_count']},
         broadcast=True)

# Sanity check! See what config is being used
# import sys
# print(app.config, file=sys.stderr)