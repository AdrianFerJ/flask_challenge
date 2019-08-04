$(document).ready(function() {

    // Set namespace to broadcast messages to
    namespace = '/test';

    // Connect to the Socket.IO server.
    var socket = io(namespace)

    // Event handler for new connections.
    // A callback func used when a connection with server is established
    socket.on('connect', function() {
        socket.emit('my_event', {data: 'Connection established!'});
    });

    // Event handler for data is emited from the server
    // Comments emited by the server are displayed in "Comments" section
    socket.on('comment_created', function(msg, cb) {
        console.log('# Server response: ', msg);
        // Append new comment (broadcasted) to Comments list
        const newComment = msg.data.id + ' ' + msg.data.email + ' ' + msg.data.username;
        $('#entries').append('<li class="comment list-group-item">' + newComment + '</li>');
        if (cb)
            cb();
    });

    // Handlers from input from user and uses socket to emit data to server
    $('form#comments').submit(function(event) {
        payload = {
            username: $('#cm-username').val(),
            email: $('#cm-email').val(),
            text: $('#cm-text').val()
        }
        console.log('# Payload: ', payload);
        socket.emit('my_comments_event', {data: payload});
        return false;
    });
});