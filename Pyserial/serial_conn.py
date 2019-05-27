"""
python AT Command Tool
"""

import threading
import serial
import time
import sys

if len(sys.argv) < 2:
    print('input the port! eg: serial_conn.py /dev/ttyS3')
    sys.exit(1)
port = sys.argv[1]
baudrate = int(sys.argv[2]) if len(sys.argv) > 2 else 115200
ser = None
try:
    ser = serial.Serial(port=str(port), baudrate=int(baudrate), rtscts=False, timeout=0.1)
    if ser.is_open:
        print('connect success')
except Exception:
    print('connect error!')
    exit()


def get_time():
    time_array = time.localtime()
    other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return other_style_time


class Response(threading.Thread):
    def __init__(self, ser_conn):
        super().__init__()
        self.ser = ser_conn
        self.flag = True

    def run(self):
        ser_conn = self.ser
        response = []
        while self.flag:
            res_bytes = ser_conn.read(100)
            for res_byte in res_bytes:
                response.append(res_byte)
                if res_byte == 10:
                    res_str = str(bytes(response)).replace('b\'', '').replace('\\r\\n\'', '')
                    response = []
                    if len(res_str) > 1:
                        print(get_time() + ':output-> ' + res_str)

    def stop(self):
        self.flag = False


res = Response(ser)
res.start()
print('q means quit!')
print('this script support AT mode(default) and DATA mode.\ninput [switch] can change current mode')
at_mode = True
while True:
    cmd = input('')
    if cmd == '':
        continue
    if cmd == 'q':
        res.stop()
        exit()
    if cmd == 'switch':
        at_mode = False if at_mode else True
        print('mode changed')
        continue
    print(get_time() + ':input-> ' + cmd)
    cmd = cmd + '\r\n' if at_mode else cmd
    ser.write(cmd.encode())
    time.sleep(1)
