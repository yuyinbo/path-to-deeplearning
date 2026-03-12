# 作者: 余殷博
# cangj87@gmail.com
# 调用相同的逻辑，但是得到不同的行为


class Cat(object):

    def __init__(self, name):
        self.name = name

    def eat(self):
        print('%s is eating fish' % self.name)


class CartoonCat(Cat):

    def eat(self):
        print('%s is eating turkey' % self.name)


class Person:

    def __init__(self, name):
        self.name = name

    def feed(self, cat):
        print("%s is feeding %s" % (self.name, cat.name))
        cat.eat()
        # cat并不一定是特定的类型，但知道有eat()方法
        # 运行时根据具体类型调用对应的eat()，这里称作多态


if __name__ == '__main__':
    kitty = Cat('Kitty')
    tom = CartoonCat('Tom')
    mark = Person('Mark')
    mark.feed(kitty)
    mark.feed(tom)
