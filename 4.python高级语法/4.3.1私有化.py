# xx: 公有变量
# _x: 不能导入别人包里的方法，单前置下划线,私有化属性或方法，from somemodule import *禁止导入,类对象和子类可以访问
# __xx：不能继承属性，双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)
# __xx__:双前后下划线,用户名字空间的魔法对象或属性。例如:__init__ , __ 不要自己发明这样的名字
# xx_:单后置下划线,用于避免与Python关键词的冲突


# 查看路径
import sys
print(sys.path)
for i in sys.path:
    print(i)

# 通过append和insert加进去

# 重新导入模块
from imp import reload

reload(sys)
import numpy

help(numpy)

# 多模块开发注意点 ✨✨
# 直接导包是全局变量  import common
# 导入包的变量是局部变量 import common.flag









