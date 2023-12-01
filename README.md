# LifeScan
A Python based ultra lightweight network segment scanning tool.
一个基于Python3的超轻量网段扫活工具
## 立即使用
```
python3 main.py <你的网段，如：192.168.1.0>
```
## 为什么选择LifeScan
### 超轻量
只有832字节的大小，再低的配置也能轻松运行
### 无需外置库
程序用到的所有库均为Python3自带库，无需外置安装
### 多线程
该程序使用了Python3自带的treading库，多线程并发，提高扫描速度
### 高兼容性
基于系统的Ping命令，内嵌于Windows和Linux
### 开源、免费
本代码全局开源免费，内容简单，小白也能进行代码审计
### 隐蔽性
Ping命令本身不会被服务器认定为攻击行为，并且命令经过作者调试，发包数量少，隐蔽性高
