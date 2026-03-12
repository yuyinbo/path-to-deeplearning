# 作者: 余殷博
# cangj87@gmail.com


def sum_2_num(num1, num2):
    """
    两个数字相加
    :param num1:
    :param num2:
    :return:
    """
    return num1 + num2
    # pass
    # 没有返回值则返回None


result = sum_2_num(3, 5.5)  # return是什么类型，返回值就是什么类型
print(result)


def test1():
    print("*" * 50)
    print("test 1")
    print("*" * 50)


def test2():
    print("-" * 50)
    print("test 2")
    test1()
    print("-" * 50)


test2()
