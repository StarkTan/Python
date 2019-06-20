import base64
import time

print(time.time())
encodestr = base64.b64encode('abcr34r344r'.encode('utf-8'))
print(time.time())
print(encodestr.decode('utf-8'))
print(base64.b64decode(encodestr))

print(base64.b64encode('hima004:123456'.encode('utf-8')))
