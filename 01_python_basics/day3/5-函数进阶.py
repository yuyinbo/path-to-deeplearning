# 作者: 余殷博
# cangj87@gmail.com

a = 1
b = 2
a, b = b, a  # python特有交换两个数的方式
# 实际上就是利用元组
print(a, b)


def return_more():
    """
    返回多个值
    :return:
    """
    return 1, 2


rets = return_more()
print(rets)
print(type(rets))
a, b = return_more()
# 利用元组
print(a)
print(b)


def print_info(name, gender=True, title=""):
    """
    使用缺省参数
    缺省参数必须是最末的参数
    :param name:
    :param gender:
    :param title:
    :return:
    """
    gender_text = "Man"
    if not gender:
        gender_text = "Woman"

    print("%s is a %s" % (name, gender_text))
    if title:
        print("%s is a %s" % (name, title))


print_info('Miko', False, "Monitor")
print_info('Steve')
