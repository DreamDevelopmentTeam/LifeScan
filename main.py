import subprocess
import sys
import threading

life_list = []
scan_list = []

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
