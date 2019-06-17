import urllib.request
import urllib.parse

url = 'http://127.0.0.1:8080/test'
data = {'param1': 'param1', 'param2': 'param2'}


def get(url, data):
    params = urllib.parse.urlencode(data)
    return urllib.request.urlopen("%s?%s" % (url, params))


def post(url, data):
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url)
    request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")
    return urllib.request.urlopen(request, data)


def put(url, data):
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, method='PUT')
    request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")
    return urllib.request.urlopen(request, data)


def delete(url, data):
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, method='DELETE')
    return urllib.request.urlopen(request, data)


print(get(url, data).read().decode('utf-8'))
print(post(url, data).read().decode('utf-8'))
print(put(url, data).read().decode('utf-8'))
print(delete(url, data).read().decode('utf-8'))
