# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 21:40:59 2019

@author: xh
"""

import socket

def main():
    # 1.买个手机:创建socket
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.插入手机卡（绑定本地信息 bind）
    tcp_server_socket.bind(("",7890))
    # 3.让默认的套接字由主动变为被动(listen)
    tcp_server_socket.listen(128)
    # 4.等待客户端的链接 accept
    new_client_socket,client_addr = tcp_server_socket.accept()
    
    print(client_addr)

    #接收客户端发送来的数据
    recv_data = new_client_socket.recv(1024)
    print(recv_data)
    #回送一部分数据给客户端
    new_client_socket.send("hahah".encode("utf-8"))
    #关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()

if __name__ == "__main__":
    main()
