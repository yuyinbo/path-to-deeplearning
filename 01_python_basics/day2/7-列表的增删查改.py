# 作者: 余殷博
# cangj87@gmail.com

name_list = ['zhangsan', 'lisi', 'wangwu']

# 查
# 1.取值、取索引和计数
print(name_list[2])
print(name_list.index('wangwu'))
print(name_list.count('zhangsan'))
print('-' * 50)

# 2.修改
name_list[1] = '李四'
print(name_list)
print('-' * 50)

# 3.增加
name_list.append('王小二')  # 追加
print(name_list)
name_list.insert(0, '王小美')  # 插入到指定位置，之后的后移
print(name_list)
temp_list = ['孙悟空', '猪悟能', '沙悟净']
print(id(name_list))
name_list.extend(temp_list)
print(name_list)
print(id(name_list))  # 将另一个列表完整拼接到本列表后面，不会改变地址
print('-' * 50)

# 4.删除
name_list.remove('王小美')  # 按元素删除
print(name_list)
name_list.pop()
print(name_list)  # 删除最后一个
name_list.pop(3)
print(name_list)  # 按位置删除
del name_list[4]
print(name_list)  # 也是按位置删除
name_list.clear()  # 清空列表
print(name_list)
print(id(name_list))  # 不会改变列表地址
