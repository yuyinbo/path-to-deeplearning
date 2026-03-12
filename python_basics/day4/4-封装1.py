# 作者: 余殷博
# cangj87@gmail.com

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

    def __str__(self):
        return f'{self.name}体重是{self.weight}kg'


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s占地%.2fm^2" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area  # 剩余面积
        self.item_list = []

    def add_item(self, item: HouseItem):  # 冒号后的类名起到注解作用
        if self.free_area >= item.area:
            self.item_list.append(item)
            self.free_area -= item.area
        else:
            print('空间不足')

    def __str__(self):
        return ("房型是%s，总面积%.2f，剩余空间%.2f，家具有%s"
                % (self.house_type, self.area, self.free_area,
                   [item.name for item in self.item_list]))


elephant = Person('大象', 18, 80)
print(elephant)
elephant.run()
elephant.eat()

# 创建家具
bed = HouseItem("床", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)
house = House('三室一厅', 70)
print(house)
house.add_item(bed)
print(house)
house.add_item(chest)
print(house)
house.add_item(table)
print(house)
