from threading import Lock
from flask import Flask, render_template, session 
from flask_socketio import SocketIO, emit

# Enable async_mode in convination with "eventlet" or "gevent"
# Set this variable to "threading"
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ShhuperSecreto!'
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