from flask_socketio import SocketIO, emit
from flask import Blueprint

comments_blueprint = Blueprint('comments', __name__)


# Enable async_mode in convination with "eventlet" or "gevent"
# Set this variable to "threading"
async_mode = None

# Websocket configuration
socketio = SocketIO(comments_blueprint, async_mode=async_mode)
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
