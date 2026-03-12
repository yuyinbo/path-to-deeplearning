# 作者: 余殷博
# cangj87@gmail.com

def test(num):
    print(num)
    if num == 1:
        print("Return here.")
        return

    test(num - 1)
    print(num)


test(3)
# 打印3，2，1，然后返回到3
