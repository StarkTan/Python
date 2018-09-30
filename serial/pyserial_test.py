import serial
ser =serial.Serial(port='/dev/ttyS3', baudrate=115200)
ser.write(b'\x01\x03\x00\x00\x00\x06\xc5\xc8')
ser.write(b'at\r\n')

print(ser.read(17))