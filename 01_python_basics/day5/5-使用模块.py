# 作者: 余殷博
# cangj87@gmail.com
import random
import my_module as mm
# 导入模块，使用别名来访问模块里的内容
from my_module import say_hello
# 导入模块里的函数，可以直接使用函数名来访问
# 用于高频方法
from my_module1 import say_hello as say_hello1
# 如果导入名称冲突的函数，必须起一个别名

from my_module1 import *

# 导入模块里的所有内容，使用时不需要模块名来访问
# 但是不建议使用，可能会有名称冲突

mm.say_hello()
# 必须使用模块名，因为已经导入了my_module1的所有内容
# 否则会调用my_module1里的say_hello函数
say_hello1()
tom = Cat()

# 想知道模块的路径
print('my_module的模块路径', mm.__file__)
print('random的模块路径', random.__file__)
