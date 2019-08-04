import os
import datetime as dt
from threading import Lock
from flask import Flask, render_template, session 
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy



# Create App
app = Flask(__name__)


# App Config
from config import DevelopmentConfig, DockerDevelopmentConfig
# app_settings = os.getenv('APP_SETTINGS')
# app.config.from_object(app_settings)
app.config.from_object(DevelopmentConfig)


db = SQLAlchemy(app)


import models

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
    entries = db.session.query(models.Comments)
    # return render_template('index.html', async_mode=socketio.async_mode)
    return render_template('index.html', entries=entries)


@socketio.on('my_comments_event', namespace='/test')
def add_new_comments(message):
    """ Endpoint to create new comments and broadcast it to subscribers"""

    session['receive_count'] = session.get('receive_count', 0) + 1

    # Parse message
    # TODO add form data validation
    username = message['data']['username']
    text = message['data']['text']
    email = message['data']['email']

    # Add new comment to db
    #TODO add (TRY) and handle failled cm creation. Send diff message and status
    new_comment = models.Comments(username=username, text=text, email=email)
    db.session.add(new_comment)
    db.session.commit()

    # Generate message if succesful comment creation    
    return_data = {
        'id': new_comment.id,
        'email': new_comment.email, 
        'username': new_comment.username,
        'text': new_comment.text, 
        'pub_date': '{:%d %B %Y}'.format(new_comment.pub_date)
    }
    return_status = 'comment_created' #'Comment created!'

    # Emit response
    emit(return_status,
        {'data': return_data, 'count': session['receive_count']},
        # {'data': return_data, 'count': session['receive_count']},
        broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
