# 作者: 余殷博
# cangj87@gmail.com


class Women:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        # 加上两个下划线，则变成了私有属性，只能在类内部被访问

    def __secret(self):
        # 私有方法，只能在类内调用
        print(self.__age)

    def parent(self):
        """
        使用公有方法简介调用私有方法，访问私有属性
        :return:
        """
        self.__secret()


if __name__ == '__main__':
    wendy = Women('Wendy', 18)
    # print(wendy.age)
    # wendy.secret()
    wendy.parent()
