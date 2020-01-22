import jwt
import time

secret = b'\x7d\xef\x87\xd5\xf8\xbb\xff\xfc\x80\x91\x06\x91\xfd\xfc\xed\x69'
expire_time = int(time.time() + 3600)  # 1 小时后超时

encoded = jwt.encode({'id': 4294967296, 'exp': expire_time}, secret, algorithm='HS256')
encoded_str = str(encoded, encoding='ascii')
print(encoded_str)

info = jwt.decode(encoded_str, secret, algorithm='HS256')
print(info)