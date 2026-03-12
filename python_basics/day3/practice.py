# 作者: 余殷博
# cangj87@gmail.com


def practice1():
    """
    有七个整数，其中三个数出现两次，一个数出现一次，找出出现一次的那个数
    :return:
    """
    num_list = [1, 2, 3, 2, 1, 6, 6]
    result = 0
    for i in num_list:
        result ^= i
    # 这能成立是因为异或满足交换律
    print(result)


def practice6():
    """
    有8个整数，其中3个出现两次，2个出现一次，找出出现一次的2个数
    :return:
    """
    num_list = [1, 1, 2, 2, 3, 8, 3, 10]
    result = 0
    for i in num_list:
        result ^= i
    # 此时i为2个只出现一次的数按位异或的结果
    split_flag = result & -result
    # 对整数x, -x == ~x + 1
    # 于是取到了result最低一位1，也就是这2个数不同的最低位为1，其他位都为0的数
    result1, result2 = 0, 0
    for i in num_list:
        if i & split_flag:  # 判断该位是否为1，以此分成分别包含两个数的两组
            result1 ^= i  # 如果该位为1，进入这里，得到两个数中该位为1的
        else:
            result2 ^= i
    print(result1, result2)


practice1()
practice6()
