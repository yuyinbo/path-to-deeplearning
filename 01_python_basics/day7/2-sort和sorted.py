# 作者: 余殷博
# cangj87@gmail.com
from operator import itemgetter, attrgetter

list1 = [1, 3, 2, 4, 5, 3, 2]

print(sorted(list1))
# sorted返回一个新的列表，不改变原列表
print(list1)
list1.sort()
print(list1)
# sort()改变原列表
print()

print(sorted({1: 'D', 2: 'B', 3: 'C', 4: 'A'}))
print()
# 排字典的时候，实际上是按key排序
str_list = "This is a test string from Andrew".split()
# 构建一个内含几个单词的列表
for i in range(len(str_list)):
    str_list[i] = str_list[i].lower()


def str_lower(str1: str) -> str:
    # 其中: str和-> str是参数的类型注解，告诉读者和静态检查工具
    """
    将字符串转换为小写
    :param str1:
    :return:
    """
    return str1.lower()


print(str_list)
print(sorted(str_list, key=str_lower))
# key = str_lower 告诉sorted先将列表里每个元素传给str_lower()转为小写再排序
# 是sorted()的回调函数
# key参数用来指定排序规则，将列表中每个元素按右侧函数处理
print()
student_tuples = [
    ('andy', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print(sorted(student_tuples))
# 默认按第一个元素排序
print(sorted(student_tuples, key=lambda x: x[2]))


# 使用匿名函数，匿名函数意思是这个函数没有名字，临时使用，后续不再使用
# lambda x: x[2]的意思是，参数是x，返回值是x[2]
# sorted(student_tuples, key=lambda x: x[2]) 是将列表每个元素传递给x
# 然后返回x[2]
# 使用匿名函数主要目的是提升阅读效率


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """
        作用类似__str__，但可以返回字符串之外的其他类型
        一般来说不应与__str__一起使用
        :return:
        """
        return repr((self.name, self.grade, self.age))


students = [
    Student('Aurora', 'A', 15),
    Student('Jane', 'B', 12),
    Student('Daniel', 'B', 10),
]

# 排序对象
print(sorted(students, key=lambda x: x.age))
# 将三个Students对象传递给x，返回x.age， 然后进行排序
print()

# 使用operator库函数自定义排序
print(sorted(student_tuples, key=itemgetter(2)))
print(sorted(students, key=attrgetter('age')))
# itemgetter()获取列表中元组中指定索引的元素
# attrgetter()获取对象中指定名字属性的值，是attribute的简写
print()

print(sorted(student_tuples, key=itemgetter(1, 2)))
# 先按照索引为1的元素排序，如果相同，则按索引为2的元素排序
# itemgetter()可用于元组，列表
print(sorted(student_tuples, key=lambda x: x[1:]))
# 将索引1，2的内容切片为元组，元素为元组的列表也可以排序，排序方法和上面相同
print(sorted(students, key=attrgetter('grade', 'age')))
# 先按属性grade排序，如果grade相同，则按age排序
print(sorted(students, key=lambda student: (student.grade, student.age)))
# 将属性grade和age取出来组成元组，和上面结果相同
print(sorted(student_tuples, key=lambda x: x[1:], reverse=True))
print(sorted(students, key=lambda student: (student.grade, student.age), reverse=True))
# reverse=True表示降序
print()

# 排序稳定性
data = [('red', 2), ('blue', 1), ('red', 1), ('blue', 2)]
print(sorted(data, key=lambda x: x[0]))
# ('red', 2)排在('red', 1)之前
# 事实上sorted是稳定的
print()

# 字典元素包含列表的情况
my_dict = {
    'Li': ['Male', 18],
    'Zhang': ['Male', 19],
    'Wang': ['Female', 16],
    'Zhou': ['Female', 20],
    'Ma': ['Male', 17]
}

for v in my_dict.items():
    # items()返回字典的键值对元组
    print(v)
print(sorted(my_dict.items(), key=lambda v: v[1][1]))
# v[1][1]意思是：
# v是列表的键值对元组，v[1]是值列表，v[1][1]是列表中的第二个元素，即年龄
print()

# 列表元素包含字典的情况
game_result = [
    {"name": "Bob", "wins": 10, "losses": 3, "rating": 75.00},
    {"name": "David", "wins": 3, "losses": 5, "rating": 57.00},
    {"name": "Carol", "wins": 4, "losses": 5, "rating": 57.00},
    {"name": "Patty", "wins": 9, "losses": 3, "rating": 71.48}]
print(sorted(game_result, key=lambda item: (item["rating"], item["name"])))
print(sorted(game_result, key=itemgetter("rating", "name")))
# itemgetter()也可以用于字典，但其中填的是字典的键
# 上面两者都意味着先按rating排序，如果rating相同，再按name排序
# sorted(game_result)无法比较字典的大小，必须制定规则
print()

# 第一项按升序，第二项按降序
tuples = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
sorted_tuples = sorted(tuples, key=lambda x: (-x[0], x[1]))
# -x[0]先将元素取相反数，对相反数排升序就相当于对原元素排降序
# 加入“-”即可控制在这里的升降序
print(sorted_tuples)
