# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:14:52 2019

@author: xh
"""
import socket

def main():
    # 1. 创建tcp的套接字
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    # 2. 连接服务器
    server_ip = '192.168.64.1'
    server_port = 8080
    tcp_client_socket.connect((server_ip,server_port))
    
    # 3. 发送数据/接收数据
    send_data = input("请输入要发送的数据：")
    tcp_client_socket.send(send_data.encode("gbk"))
    
    recvData = tcp_client_socket.recv(1024)
    print(recvData.decode('gbk'))
    
    # 4. 关闭套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    main()

