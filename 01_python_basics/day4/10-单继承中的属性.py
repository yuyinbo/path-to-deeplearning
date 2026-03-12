# 作者: 余殷博
# cangj87@gmail.com

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + ' eats')

    def drink(self):
        print('drink')

    def run(self):
        print('run')

    def sleep(self):
        print('sleep')


class Dog(Animal):
    # 继承父类(Animal)的所有属性和方法
    def bark(self):
        print(self.name+' braks')


class Cat(Animal):
    def __init__(self, name, color):
        """
        继承父类的属性并添加新的属性
        :param name:
        :param color:
        """
        super().__init__(name)
        self.color = color

    def talk(self):
        print(self.name + ' is talking')


if __name__ == '__main__':
    a = Animal('Mark')
    a.eat()
    d = Dog('Taroumaru')
    d.bark()
    # Dog里没有__init__，则调用父类的
    print()
    c = Cat('Tom', 'blue')
    c.talk()
