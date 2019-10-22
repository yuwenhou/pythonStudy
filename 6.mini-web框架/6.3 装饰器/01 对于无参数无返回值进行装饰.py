def set_func(func):

    def call_func():
        print("----这是权限验证1-----")
        func()

    def error():
        print("密码错误")
    # return call_func
    password = input("请输入你的密码")
    if password == "123456":
        return call_func
    else:
        return error

@set_func # 等价于test1 = set_func(test1)
def test1():
    print("-------test1-------")


test1()




