import os
from threading import Lock
from flask import Flask, render_template, session 
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
import models

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
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)

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
    return render_template('index.html', async_mode=socketio.async_mode)


@socketio.on('my_comments_event', namespace='/test')
def broadcast_comments(message):
    """ Namespace channel to recieve and emit new comments from & to client"""

    session['receive_count'] = session.get('receive_count', 0) + 1

    # Parse message
    title = message['data']['title']
    text = message['data']['text']
    payload = title + ', ' + text

    emit('my_response',
         {'data': payload, 'count': session['receive_count']},
         broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)