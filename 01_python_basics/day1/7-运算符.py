# 作者: 余殷博
# cangj87@gmail.com


def use_cal():
    """
    算术运算符
    :return:
    """
    result = 5 / 2
    print(result)
    result = 5 // 2  # 整除
    print(result)
    result = 5 % 2  # 取模
    print(result)
    result = 10 % 2 ** 2  # 幂次运算符是算术运算符中优先级最高的
    print(result)


def use_logic():
    """
    逻辑运算符
    :return:
    """
    print(3 and 5)  # 都真返回后一个
    print(0 and False)  # 都假返回前一个（短路运算）
    print(True or 1)  # 都真返回前一个（短路运算）
    print(False or 0)  # 都假返回后一个
    a = 5
    a > 5 and print('a大于5')  # 如果前一个为假，不会运算后面（短路运算）
    b = 5
    b > 1 or print('b等于1')  # 如果前一个为真，不会运算后面（短路运算）


def use_bit():
    """
    位运算符
    :return:
    """
    # python的整数是自动扩展的
    a = 5  # 0000 0101
    b = 7  # 0000 0111
    print(a & b)  # 0000 0101
    print(a | b)  # 0000 0111
    print('-' * 50)
    print(a << 2)  # 0001 0100
    print(-10 >> 1)  # 1111 0110->1111 1011
    print(-9 >> 1)  # 1111 0111->1111 1011 减一除以二
    print(-1 >> 1111111)  # 1111 1111->1111 1111 每移动一位，减一除以二
    print(~a)  # 1111 1010, 按位取反再加一才是-a的补码
    print('-' * 50)
    print(5 ^ 7 ^ 5)  # 异或运算满足交换律，任何数与自己异或为0，任何数与0异或为自身


use_cal()
use_logic()
use_bit()
