# 作者: 余殷博
# cangj87@gmail.com
import my_first_module  # 名字不再是__main__

my_first_module.print_line('-', 80)
print(my_first_module.char1)  # 访问不了只在模块内可见的全局变量
