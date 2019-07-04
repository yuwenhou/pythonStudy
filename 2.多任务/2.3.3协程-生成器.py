def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a  # 如果一个函数中yield语句，那么这个就不再是函数，而是一个生成器模板
        a, b = b, a+b
        current_num += 1
    return "ok...."
# 如果在调用create_num的时候，发现这个函数中有yield那么此时，不是调用函数，而是创建一个生成器对象
obj = create_num(100)

# for num in obj:
#     print(num)

while True:
    try:
        ret = next(obj)
        print(ret)
    except Exception as ret:
        print(ret.value)
        break
