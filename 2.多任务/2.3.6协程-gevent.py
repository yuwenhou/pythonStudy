"""
# demo1

import gevent


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()
"""
"""
demo2
"""

from gevent import monkey
import gevent
import random
import time

# 有耗时操作的需要
monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块


def corotine_work(corotine_name):
    for i in range(10):
        print(corotine_name, i)
        time.sleep(random.random())


gevent.joinall([
    gevent.spawn(corotine_work, "work1"),
    gevent.spawn(corotine_work, "work1")
])
