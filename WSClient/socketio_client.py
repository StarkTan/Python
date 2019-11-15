import socketio

sio = socketio.Client()
start_timer = None

sio.connect(url='http://localhost:5000', namespaces='/socket_io/test')

def server_response(data):
    print(data)

sio.on('server_response',handler=server_response,namespace='/socket_io/test')
sio.emit('client_event', {'data': 123}, namespace='/socket_io/test')

sio.wait()

