# 作者: 余殷博
# cangj87@gmail.com

class Animal:
    def eat(self):
        print('eat')

    def drink(self):
        print('drink')

    def run(self):
        print('run')

    def sleep(self):
        print('sleep')


class Dog(Animal):
    # 继承父类(Animal)的所有属性和方法
    def bark(self):
        print('brak')


class Cat(Animal):
    def catch(self):
        print('catch')


class Taroumaru(Dog):
    # 继承Dog，而没有继承Cat
    def fight(self):
        print('fight')

    def bark(self):
        """
        对父类的方法进行重写(override)
        :return:
        """
        super().bark()
        # 先调用一次父类中的bark()
        # 如果父类中没有（没有重写），则找祖父类
        # super()称作匿名父类对象，从当前类在 MRO 中的位置往后找方法
        print('bark loudly')


if __name__ == '__main__':
    a = Animal()
    a.sleep()
    print()
    d = Dog()
    d.eat()
    d.bark()
    print()
    c = Cat()
    c.catch()
    print()
    t = Taroumaru()
    t.fight()
    # t.catch()
    # Taroumaru没有继承Cat
    t.bark()
    # 和一般的Dog叫声不同
