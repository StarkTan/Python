import os
import re
import threading
import time

def get_gateway_win():
    """获取网关的IP,不完整只能获取第一个网关IP"""
    cmd = 'ipconfig/all|find "IPv4"'
    lines = os.popen(cmd).readlines()
    if lines:
        for line in lines:
            result = re.findall(
                r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", line)
            if result:
                return result[0]


def get_gateway_linux(net_ifac = None):
    if net_ifac is None:
        cmd = 'netstat -rn'
    else:
        cmd = 'netstat -rn |grep %s'%net_ifac
    lines = os.popen(cmd).readlines()
    if lines:
        for line in lines:
            result = re.findall(
                r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", line)
            if result:
                return result[0]


def valid_ip_mac(ip):
    ping_cmd = 'ping -n 2 {}|find "100%"'.format(ip)
    lines = os.popen(ping_cmd).readlines()
    if lines:
        return None
    arp_cmd = 'arp -a {}|find "{}"'.format(ip,ip)
    lines = os.popen(arp_cmd).readlines()
    if lines:
        result = re.findall(
            r'[0-9a-f]{2}-[0-9a-f]{2}-[0-9a-f]{2}-[0-9a-f]{2}-[0-9a-f]{2}-[0-9a-f]{2}', lines[0])
        if result:
            return str(result[0]).replace('-', '').upper()


def find_all_valid_ip_mac():
    gateway = get_gateway_win()
    if gateway is None:
        return
    index = str(gateway).rindex('.')
    ip_pre = str(gateway)[0:index+1]
    for i in range(2,255):
        ip = ip_pre+str(i)
        mac = valid_ip_mac(ip)
        if mac:
            print(ip, mac)


def arp_a_win(gateway=None):
    if gateway is None:
        gateway = get_gateway_win()
    if gateway is None:
        return
    index = str(gateway).rindex('.')
    ip_pre = str(gateway)[0:index + 1]

    cmd = 'arp -a'
    lines = os.popen(cmd).readlines()
    res = []
    for line in lines:
        ip = None
        mac = None
        result = re.findall(
            r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", line)
        if result:
            ip = result[0]
        result = re.findall(
            r'[0-9a-f]{2}-[0-9a-f]{2}-[0-9a-f]{2}-[0-9a-f]{2}-[0-9a-f]{2}-[0-9a-f]{2}', line)
        if result:
            mac = str(result[0]).replace('-', '').upper()
        if not ip is None and not mac is None and ip_pre in ip:
            res.append((ip, mac))
    return res


def arp_a_linux(gateway=None):
    if gateway is None:
        gateway = get_gateway_linux('wlan0')
    if gateway is None:
        return
    index = str(gateway).rindex('.')
    ip_pre = str(gateway)[0:index + 1]

    cmd = 'arp -a'
    lines = os.popen(cmd).readlines()
    res = []
    for line in lines:
        ip = None
        mac = None
        result = re.findall(
            r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", line)
        if result:
            ip = result[0]
        result = re.findall(
            r'[0-9a-f]{2}-[0-9a-f]{2}-[0-9a-f]{2}-[0-9a-f]{2}-[0-9a-f]{2}-[0-9a-f]{2}', line)
        if result:
            mac = str(result[0]).replace('-', '').upper()
        if not ip is None and not mac is None and ip_pre in ip:
            res.append((ip, mac))
    return res


def ping_all_ip():
    global current
    current = 0

    def get_next():
        global current
        current += 1
        return current

    def ping():
        num = get_next()
        while num < 225:
            cmd = 'ping -n 1 192.168.10.%d' % num
            os.popen(cmd).readlines()
            # print(cmd)
            num = get_next()
    threads_live = []
    for i in range(224):
        thread = threading.Thread(target=ping)
        thread.start()
        threads_live.append(thread)
    while threads_live:
        temp = []
        for thread in threads_live:
            if thread.is_alive():
                temp.append(thread)
        threads_live = temp


print(time.time())
ping_all_ip()
print(time.time())
print(arp_a_win())
print(time.time())


# print(arp_a_win())
# find_all_valid_ip_mac()
