def set_func(func):

    def call_func(num,*args,**kwargs):
        password = input("请输入你的密码")
        if password == "123":
            print("----这是权限验证1-----")
            func(num,*args,**kwargs)
        else:
            print("密码错误")
    # return call_func

    return call_func

@set_func # 等价于test1 = set_func(test1)
def test1(num,*args,**kwargs):
    print("-------test1-------%s"%num)
    print("-------test1-------", args)
    print("-------test1-------", kwargs)



@set_func
def test2(num):
    print("------test2---------%s"%num)

test1(100,100,100,1001,123,aa=1,bb=2)
test2(371956749015)



