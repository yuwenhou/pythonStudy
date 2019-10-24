def add_qx(func):
    print("----开始进行装饰权限add的功能")
    def call_func(*args,**kwargs):
        print("----add-----")
        # func(args, kwargs) #相当于传递了2个参数：1个元组，1个字典
        return func(*args,**kwargs) # 拆包
    return call_func

def set_func(func):
    def call_func(*args, **kwargs):
        print("----set_func-----")
        return func(*args,**kwargs) # 拆包
    return call_func

@add_qx
@set_func # 等价于test1 = set_func(test1)
def test1(num,*args,**kwargs):
    print("-------test1-------%s"%num)
    print("-------test1-------", args)
    print("-------test1-------", kwargs)
    return 'ok'


ret = test1(100,100,100,1001,123,aa=1,bb=2)
print(ret)






