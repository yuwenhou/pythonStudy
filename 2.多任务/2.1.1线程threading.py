# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:12:18 2019

@author: xh
"""
import time
import threading #线程

def sing():
    """唱歌5秒"""
    for i in range(5):
        print("----正在唱歌：菊花茶----")
        time.sleep(1)
 
def dance():
    """跳舞5秒"""
    for i in range(5):
        print("----正在跳舞----")
        time.sleep(1)

def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())
        if len(threading.enumerate())<=1:
            break
        time.sleep(1)

if __name__ == "__main__":
    main()
