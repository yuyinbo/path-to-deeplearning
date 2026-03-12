# 作者: 余殷博
# cangj87@gmail.com

# 所有属于同一类的对象的方法只有一份，但各自有各自的属性
class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print(f'{self.name}跑步，体重减少了0.5kg，变成了{self.weight}')

    def eat(self):
        self.weight += 2
        print(f'{self.name}吃了顿大餐，体重增加了2kg，变成了{self.weight}')


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print(f'{self.name}汪汪叫')

    def shake(self):
        pass


if __name__ == '__main__':
    elephant = Person('大象', 18, 80)  # 实例化对象
    tiger = Person('老虎', 17, 60)

    elephant.run()  # 调用方法, 此时一定会把对象自身传进去
    # 如果在定义里不写run(self)会出错
    elephant.eat()
    elephant.height = 1.85
    print(elephant.height)
    # 对象是可变数据类型
    # 可以在初始化之后再添加属性，但不推荐这样
    print('-' * 50)
    print(dir(Person))
    print(dir(elephant))

    print(dir(tiger))
    # 查看类或对象的所有属性与方法

    wangcai = Dog('旺财', 'yellow')
    wangcai.bark()
