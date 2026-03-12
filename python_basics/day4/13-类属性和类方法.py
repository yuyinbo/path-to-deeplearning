# 作者: 余殷博
# cangj87@gmail.com


class Tool:
    count = 0

    # 写在__init__外面的属性就是类属性，所有该类对象共用

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod
    # 标明下面是类方法
    def show_tool_count(cls):
        # 传递的不是对象而是类名
        print(cls.count)

    @staticmethod
    # 标明下面是静态方法
    # 既不需要访问实例属性或调用实例方法，也不需要访问类属性或者调用类方法
    def help():
        print("There is many tools here.")


if __name__ == '__main__':
    tool1 = Tool('axe')
    tool2 = Tool('hammer')
    tool3 = Tool('shovel')
    print(Tool.count)
    print(tool1.count)
    # 每个该类对象都有一个该属性
    # 访问属性时，先在对象查找有没有对应属性，再找类属性
    tool3.count = 99
    # 实际上增加了一个同名对象属性，没有更改类属性
    print("tool3.count = %d" % tool3.count)
    print("tool.count = %d" % Tool.count)
    Tool.show_tool_count()
    Tool.help()
    # 通过类名来访问静态方法