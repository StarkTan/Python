"""
用于测试的http服务
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello world"


app.run(host='0.0.0.0', port=80)
