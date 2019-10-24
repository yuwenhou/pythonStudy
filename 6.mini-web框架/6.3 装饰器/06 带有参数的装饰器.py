def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("权限级别10")
            elif level_num == 2:
                print("权限级别2")
            return func()
        return call_func
    return set_func

@set_level(1)
def test1():
    print("----test1-----")
    return "OK1"


@set_level(2)
def test2():
    print("----test2-----")
    return "OK2"

test1()
print(test2())
