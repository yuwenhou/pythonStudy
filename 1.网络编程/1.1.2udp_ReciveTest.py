# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:41:15 2019

@author: xh
"""
import socket

# 1.创建套接字
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 2.绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
local_addr = ('',7788) #ip地址和端口号，ip一般不用写，表示本机的任何一个ip
udp_socket.bind(local_addr)

# 3.等待接收对方发送的数据
recv_data = udp_socket.recvfrom(1024) #表示本次接受的最大字节数

# 4.显示接收到的数据
print(recv_data[0].decode('gbk'))

# 5.关闭套接字
udp_socket.close()

