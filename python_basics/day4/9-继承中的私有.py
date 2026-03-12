# 作者: 余殷博
# cangj87@gmail.com


class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test(self):
        print(self.num1, self.__num2)


class B(A):
    def demo(self):
        # print(self.num1, self.__num2)
        # 继承了父类的共用属性和方法，但不能直接访问父类的私有属性和方法
        self.test()


if __name__ == '__main__':
    a = A()
    b = B()
    a.test()
    b.demo()
