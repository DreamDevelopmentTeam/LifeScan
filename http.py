import subprocess
import sys
import threading
import requests

life_list = []
http_alive_list = []
scan_list  = []
try:
    net = sys.argv[1]
except:
    print("缺少参数")
    sys.exit()


def scan(ip):
    result = subprocess.run(['ping', '-w', '500', '-n', '2', ip], stdout=subprocess.PIPE)
    if result.returncode == 0:
        print(ip, "is alive")
        life_list.append(ip)
        http_scan(ip)


def http_scan(ip):
    try:
        response = requests.get(f'http://{ip}:80')
        if response.status_code == 200:
            print(f'{ip} HTTP(80) is alive')
            http_alive_list.append(ip)
    except requests.exceptions.RequestException as e:
        pass


net_split = net.split('.')
if len(net_split) != 4:
    print("网段错误")
    sys.exit()
net_1 = net_split[0]
net_2 = net_split[1]
net_3 = net_split[2]
net_4 = net_split[3]
for i in range(1, 255):
    ip = net_1 + '.' + net_2 + '.' + net_3 + '.' + str(i)
    t = threading.Thread(target=scan, args=(ip,))
    scan_list.append(t)
    t.start()
# 等待所有线程结束
for t in scan_list:
    t.join()

print("存活主机：", life_list)
print("存活并支持HTTP(80)的主机：", http_alive_list)
