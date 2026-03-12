# 作者: 余殷博
# cangj87@gmail.com

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print("%s来了" % self.name)

    def __del__(self):
        """
        回调函数，用于记录对象被销毁的记录
        :return:
        """
        print("%s走了" % self.name)

    def __str__(self):
        """
        需要返回字符串类型
        使打印对象时，输出的是这个函数的返回值
        :return:
        """
        return self.name+' is a '+self.color+' cat.'


tom = Cat('Tom', 'blue')
print(tom)
del tom  # 如果不在此处销毁，则会在程序结束后销毁
print('程序结束')
