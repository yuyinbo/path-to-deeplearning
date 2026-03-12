# 作者: 余殷博
# cangj87@gmail.com


class A:
    def test(self):
        print("A.test()")


class B:
    def test(self):
        print("B.test()")

    def demo(self):
        print("B.demo()")


class C(A, B):
    def test(self):
        print("C.test()")
        super().test()  # 取到的是MRO后面一个


if __name__ == '__main__':
    c = C()
    c.test()
    c.demo()
    print(C.__mro__)
    # 先从本类查找，再从A，再从B查找
    # mro() 返回一个列表
    # __mro__是类的一个属性
