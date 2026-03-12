# 作者: 余殷博
# cangj87@gmail.com


info_tuple = ("zhangsan", 18, 1.75, "zhangsan")
# 1. 取值和取索引
print(info_tuple[0])
# 找到第一个该元素的索引
print(info_tuple.index("zhangsan"))
# 2. 统计计数
print(info_tuple.count("zhangsan"))
# 统计元组中包含元素的个数
print(len(info_tuple))
# 3.转换类型
print(info_tuple)
print(list(info_tuple))

print('-'*50)
for info in info_tuple:
    print(info)

info_tuple = ("小明", 21, 1.85)
# 格式化字符串后面的 `()` 本质上就是元组
print("%s 年龄是 %d 身高是 %.2f" % ("小明", 21, 1.85))
# 等价于
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)
# 等价于
info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
print(info_str)
# 等价于
info_str = "{} 年龄是 {} 身高是 {}".format(*info_tuple)
print(info_str)
