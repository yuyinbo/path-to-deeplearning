# 作者: 余殷博
# cangj87@gmail.com


def practice4():
    """
    奇数求和
    :return:
    """
    lst = [x for x in range(1, 101) if x % 2 == 1]
    print(sum(lst, 0))


def practice5():
    """
    打印九九乘法表
    :return:
    """
    lst = [[f'{i}*{j}={i * j:<3d}' for i in range(1, j + 1)] for j in range(1, 10)]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j], end="")
        print()


def practice6_1():
    """
    统计一个整数对应二进制数的1的个数
    :return:
    """
    num = int(input('请输入一个整数: '))
    if num >= 0:
        print(bin(num).count('1'))
    else:
        print(64 - bin(~num).count('1'))
        # 因为负数x，-x和x补码的1个数相加为64


def practice6_2():
    """
    截断为64位补码
    :return:
    """
    num = int(input('请输入一个整数: '))
    print(bin(num & 0xffffffffffffffff).count('1'))
    # 截取低64位，就是模拟64位补码


def practice6_3():
    """
    使用位运算
    :return:
    """
    num = int(input('请输入一个整数: '))
    count = 0
    for i in range(64):
        if num & 1:
            count += 1
        num >>= 1
    print(count)
    # 右移一次，如果最低位是1就知道了原数字有个1


def practice6_4():
    """
    使用更简单的位运算
    :return:
    """
    num = int(input('请输入一个整数: '))
    num &= 0xffffffffffffffff
    count = 0
    while num:
        num &= num - 1  # 每次可以消去最低位的一个1
        # 这是因为...1000000-1=...0111111，只保留公共的1
        count += 1
    print(count)


practice4()
practice5()
# practice6_1()
# practice6_2()
# practice6_3()
practice6_4()
