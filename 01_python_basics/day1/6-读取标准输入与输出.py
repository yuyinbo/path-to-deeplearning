# 作者: 余殷博
# cangj87@gmail.com


def use_input():
    """
    读取标准输入
    :return:
    """
    while True:
        a = input('请输入一个数据：')
        print(a)
        print(type(a))
        b = float(a)
        c = int(a)
        # 如果是str表示的小数，则需要先转成float再转成int


# use_input()
def use_print():
    name = 'xiaoming'
    stu_no = 1001
    price = 98.1
    weight = 4.666
    money = price * weight
    scale = 0.012
    print("我的名字叫 %s，请多多关照！" % name)
    print("我的学号是 %06d" % stu_no)
    print("苹果单价 %.02f 元／斤，购买 %.02f 斤，需要支付 %.02f 元" % (price, weight, money))
    print("数据比例是 %.02f%%" % (scale * 100))  # 输出%需要用%%
    # 使用f格式
    print(f"苹果单价{price:.02f}元/斤，购买{weight:.02f}斤")


use_print()
