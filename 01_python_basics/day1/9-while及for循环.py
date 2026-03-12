# 作者: 余殷博
# cangj87@gmail.com


def use_while():
    i = 1
    while i <= 5:
        print("Hello Python")
        i += 1
    print("现在 i = %d" % i)


def sum_100():
    i = 1
    result = 0
    while i <= 100:
        if i % 2 == 1:
            i += 1
            continue
        result += i
        i += 1
    print("result = %d\n最后 i = %d" % (result, i))


def sum_break():
    i = 1
    result = 0
    while i <= 100:
        if result >= 4900:
            break
        result += i
        i += 1
    print(f"result = {result}\n最后一次加入的 i = {i - 1}")


def use_for():
    """
    for必须接一个可迭代对象，必须与in组合
    :return:
    """
    my_list = [1, 2, 3]  # 列表是可迭代对象
    for i in my_list:
        print(i, end=' ')  # end默认为\n，改为空格


def use_for_else():
    i = 0
    for i in range(10):  # range是从0到9
        if i == 15:
            print('i have 15')
            break
        print(i, end=" ")
    else:
        # for循环，只要不是从break出来就从else出来
        print('don\'t find 15')
        print(f'i after loop={i}')


use_while()
sum_100()
sum_break()
use_for()
print('\n')
use_for_else()
