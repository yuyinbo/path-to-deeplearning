# 作者: 余殷博
# cangj87@gmail.com


xiaoming_dict = {"name": "小明"}
print(id(xiaoming_dict))

# 1. 取值
print(xiaoming_dict["name"])
# 在取值的时候，如果指定的 key 不存在，程序会报错
# print(xiaoming_dict["name123"])
print(xiaoming_dict.get("name123"))
# 但使用dict.get(), 如果key不存在，就不会报错, 而是返回None
print('-'*50)

# 2. 增加/修改
# dict.setdefault()，如果key存在，不会修改值； 如果key不存在，会新增键值对
xiaoming_dict.setdefault("name", "小小明")
xiaoming_dict.setdefault("QQ", "123456")
print(f"setdefault={xiaoming_dict}")
print()
# 如果 key 不存在，会新增键值对
xiaoming_dict["age"] = 18
# 如果 key 存在，会修改已经存在的键值对
xiaoming_dict["name"] = "小小明"
print(xiaoming_dict)
print(id(xiaoming_dict))  # 字典是可变数据类型

# 3. 删除
xiaoming_dict.pop("name")
# 或del xiaoming_dict["name"]
# xiaoming_dict.pop("name123")
# 与dict.get()不同，这个若key不存在会报错
print(xiaoming_dict)
print(id(xiaoming_dict))

print('-' * 50)

xiaoming_dict = {"name": "小明"}
print(id(xiaoming_dict))  # 重新赋值会改变id，就算和原先一模一样
# 而对于不可变数据类型，如果重新赋值成和原来一模一样的值，id不会变

print('-' * 50)

xiaoming_dict = {"name": "小明", "age": 18}
# 1. 统计键值对数量
print(len(xiaoming_dict))
# 2. 合并字典
temp_dict = {"height": 1.75, "age": 20}
# 如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
xiaoming_dict.update(temp_dict)
print(xiaoming_dict)
# 3. 清空字典
xiaoming_dict.clear()
print(xiaoming_dict)

print('-' * 50)

xiaoming_dict = {"name": "小明", "QQ": "123456", "phone": "10086"}
# 遍历
# 变量k是每一次循环中，获取到的键值对的key
for k in xiaoming_dict:
    print("%s - %s" % (k, xiaoming_dict[k]))
# 获取值
for v in xiaoming_dict.values():
    print(v)

# dict.items()包含的是键值对元组
for kv in xiaoming_dict.items():
    print(kv)
for k, v in xiaoming_dict.items():  # 拆包
    print(k, v)

# 以上都是“动态视图对象”，而不是列表

print('-' * 50)

# 将多个字典放在一个列表中，再进行遍历
card_list = [
    {"name": "张三",
     "QQ": "12345",
     "phone": "110"},
    {"name": "李四",
     "QQ": "54321",
     "phone": "10086"}
]
for card_info in card_list:
    print(card_info)
    for k, v in card_info.items():
        print(k, v)
