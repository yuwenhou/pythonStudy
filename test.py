def sum_numbers(num):
    print('num:%d' % num)
    if num == 1:
        return 1
    temp = sum_numbers(num - 1)
    print('-----temp:%d' % temp)
    return num + temp


result = sum_numbers(10)
print(result)
