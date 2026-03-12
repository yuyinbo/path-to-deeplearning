# 作者: 余殷博
# cangj87@gmail.com
# 字符串是不可变类型，方法实际上返回了一个新字符串


def use_str():
    str1 = "Hello Python"
    for c in str1:
        print(c, end=" ")
    # 可遍历
    print()
    print(str1.find('ll'))
    # 找到子串索引
    print(str1.replace('l', 'L', 1))
    # 从开头替换指定次数某字符

    print()
    str_list = str1.split("o", 1)
    # 按照某字符分割字符串(指定次数），返回列表，默认按空格分割
    print(str_list)

    str2 = 'hello\nworld\nhow are you\ntoday is a good day'
    str_list = str2.splitlines()
    # 按行分割，相当于str.split("\n")
    print(str_list)

    str3 = ' '.join(str_list)
    # 用指定字符串把字符串列表拼接起来，返回一个字符串
    print(str3)


def str_reverse():
    """
    反转字符串
    :return:
    """
    str4 = 'hello'
    my_list = list(str4)
    my_list.reverse()
    print(''.join(my_list))


use_str()
str_reverse()
