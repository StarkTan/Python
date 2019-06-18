import urllib.request
import urllib.parse


def get(url, data, headers={}):
    params = urllib.parse.urlencode(data)
    request = urllib.request.Request("%s?%s" % (url, params), method='GET')
    for key in headers:
        request.add_header(key, headers[key])
    return urllib.request.urlopen(request)


def post(url, data, headers={}):
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, method='POST')
    request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")
    for key in headers:
        request.add_header(key, headers[key])
    return urllib.request.urlopen(request, data)


def put(url, data, headers={}):
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, method='PUT')
    request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")
    for key in headers:
        request.add_header(key, headers[key])
    return urllib.request.urlopen(request, data)


def delete(url, data, headers={}):
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, method='DELETE')
    for key in headers:
        request.add_header(key, headers[key])
    return urllib.request.urlopen(request, data)


url = 'http://127.0.0.1:8080/test'
data = {'param1': 'param1', 'param2': 'param2'}
print(get(url, data).read().decode('utf-8'))
print(post(url, data).read().decode('utf-8'))
print(put(url, data).read().decode('utf-8'))
print(delete(url, data).read().decode('utf-8'))

headers = {'Authorization': 'Basic aGltYTAwNDpoaW1hMTIzNDU2'}
url1 = 'http://192.168.1.1:8000/wlan/listwlan'
print(get(url1, data, headers).read().decode('utf-8'))
