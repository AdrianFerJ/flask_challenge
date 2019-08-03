from flask import Flask, render_template, session, request, \
    copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

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
    return render_template('index.html', async_mode=socketio.async_mode)

if __name__ == '__main__':
    socketio.run(app, debug=True)