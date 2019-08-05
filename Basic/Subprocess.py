import subprocess
import threading


class Response(threading.Thread):
    def __init__(self, ser):
        super().__init__()
        self.ser = ser
        self.flag = True

    def run(self):
        ser = self.ser
        res = []
        while self.flag:
            res_bytes=ser.read(1)
            for res_byte in res_bytes:
                res.append(res_byte)
                if res_byte == 10 or res_byte == 35:
                    res_str = bytes(res).decode('utf-8').strip()
                    res = []
                    print(res_str)

    def stop(self):
        self.flag = False


process = subprocess.Popen('python E:\SVN\study\Python\Basic\echo.py',
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
res = Response(process.stdout)
res.start()
while True:
    data = input('')
    process.stdin.write((data+'\n').encode())
    process.stdin.flush()
