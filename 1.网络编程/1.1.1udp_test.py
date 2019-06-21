# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:09:42 2019

@author: xh
"""
import socket

def main():
	# 1. 创建一个udp套接字
   udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	# 2. 准备接受方的地址
   dest_addr = ('192.168.64.1',8080) # 注意 是元组，ip是字符串，端口是数字
   
   while True:
       # 3.从键盘获取数据
       send_data = input("请输入发送的内容:")
    
    	# 4. 发送数据到指定电脑上的直送程序中
       udp_socket.sendto(send_data.encode('utf-8'),dest_addr)

	# 5. 关闭套接字
   udp_socket.close()
   print('--run-----')

if __name__ == '__main__':
	main()


