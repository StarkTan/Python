import socketio
import time
import threading
def server_response(data):
    print(data)


def open_socket_io(sio):
    sio.connect(url='http://192.168.1.1:8000', namespaces='/gsensor')
    sio.on('server_gsensor_response', handler=server_response,namespace='/gsensor')
    sio.emit('client_request', 'start', namespace='/gsensor')
    sio.wait()
    print('''x''')


sio = socketio.Client()

threading.Thread(target=open_socket_io, args=(sio,)).start()

time.sleep(10)

sio.eio.disconnect()  # 测试发现：需要手动关闭eio  线程结束