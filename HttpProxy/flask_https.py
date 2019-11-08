"""
用于测试的https服务
创建自己证书的指令
# 生成私钥，按照提示填写内容
openssl genrsa -des3 -out server.key 1024
# 生成csr文件 ，按照提示填写内容
openssl req -new -key server.key -out server.csr
# Remove Passphrase from key
cp server.key server.key.org
openssl rsa -in server.key.org -out server.key
# 生成crt文件，有效期1年（365天）
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello world"


app.run(host='0.0.0.0', port=443, ssl_context=('cache/server.crt', 'cache/server.key'))
