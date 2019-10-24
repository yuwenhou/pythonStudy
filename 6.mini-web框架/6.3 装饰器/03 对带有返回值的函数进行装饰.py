def set_func(func):

    def call_func(*args,**kwargs):
        password = input("请输入你的密码")
        if password == "123":
            print("----这是权限验证1-----")
            # func(args, kwargs) #相当于传递了2个参数：1个元组，1个字典
            return func(*args,**kwargs) # 拆包
        else:
            print("密码错误")
            return '啦啦啦'
    # return call_func
    return call_func

@set_func # 等价于test1 = set_func(test1)
def test1(num,*args,**kwargs):
    print("-------test1-------%s"%num)
    print("-------test1-------", args)
    print("-------test1-------", kwargs)
    return 'ok'


ret = test1(100,100,100,1001,123,aa=1,bb=2)
print(ret)






