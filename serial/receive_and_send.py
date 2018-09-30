import serial
import threading

ser = serial.Serial(port='COM3', baudrate=9600)


class SendFile(threading.Thread):
    def __init__(self, ser):
        threading.Thread.__init__(self)
        self.ser = ser

    def run(self):
        ser = self.ser
        file = open('test')
        while True:
            data = file.read(1024)
            ser.write(data.encode())


class SaveFile(threading.Thread):
    def __init__(self, ser):
        threading.Thread.__init__(self)
        self.ser = ser

    def run(self):
        ser = self.ser
        count = 0
        file = open('test.txt', 'wb')
        while True:
            data = ser.read(1024)
            if data:
                count += len(data)
                file.write(data)
            print(count)


SendFile(ser).start()
SaveFile(ser).start()
