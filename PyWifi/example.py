import pywifi
import time


wifi = pywifi.PyWiFi()  # 定义接口操作
iface = wifi.interfaces()[0]  # 这里iface就是获取的wifi接口
# print(iface.name())  # wifi 模块的名称
status = iface.status()  # wifi的模块的状态  定义 pywifi.const line 7-11
if status == pywifi.const.IFACE_CONNECTED:
    iface.disconnect()  # 断掉当前连接

wifi_records = iface.network_profiles()  # 已有的无线网络配置 [pywifi.profile.Profile]
if len(wifi_records) > 0:
    iface.remove_all_network_profiles()  # 移除已有网络配置

iface.scan()  # 开始扫描附件的AP
time.sleep(5)
aps = iface.scan_results()  # 获取上次扫描的结果

ap: pywifi.profile.Profile = None
for ap in aps:
    # print(ap.bssid)  # ap的mac地址
    print(ap.ssid)   # ap的名称
    # print(ap.signal)  # ap的信号质量
    if ap.ssid == 'StarkTan':
        break
    ap = None
if ap:
    print('找到指定AP，尝试进行连接')
    pwd_dict = ['1231241231', '124123111', 'tsh123456']
    tar_pwd = None
    for pwd in pwd_dict:
        profile = pywifi.Profile()  # 定义配置文件对象
        profile.ssid = ap.ssid  # wifi名称，貌似不能用中文？
        profile.auth = pywifi.const.AUTH_ALG_OPEN  # auth - AP的认证算法
        profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)  # 选择wifi加密方式  akm - AP的密钥管理类型
        profile.cipher = pywifi.const.CIPHER_TYPE_CCMP  # cipher - AP的密码类型
        profile.key = pwd  # wifi密钥 如果无密码，则应该设置此项CIPHER_TYPE_NONE
        print('尝试使用密码：%s'% pwd)
        tmp_profile = iface.add_network_profile(profile)
        iface.connect(tmp_profile)
        time.sleep(1)
        # 测试表示正常连接速度很快
        # while iface.status() == pywifi.const.IFACE_CONNECTING:
        #     time.sleep(1)
        if iface.status() == pywifi.const.IFACE_CONNECTED:
            tar_pwd = pwd
            break
        iface.remove_network_profile(tmp_profile)
    if tar_pwd:
        print('连接成功，密码: %s'%tar_pwd)
    else:
        print('尝试连接失败')

else:
    print('未找到指定AP，程序结束')
