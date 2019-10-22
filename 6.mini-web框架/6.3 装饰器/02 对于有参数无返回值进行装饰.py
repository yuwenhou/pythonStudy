def set_func(func):

    def call_func(num):
        password = input("请输入你的密码")
        if password == "123":
            print("----这是权限验证1-----")
            func(num)
        else:
            print("密码错误")
    # return call_func

    return call_func

@set_func # 等价于test1 = set_func(test1)
def test1(num):
    print("-------test1-------%s"%num)


test1(100)




