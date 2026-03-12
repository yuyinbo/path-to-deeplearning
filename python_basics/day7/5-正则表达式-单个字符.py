# 作者: 余殷博
# cangj87@gmail.com
import re

# 匹配案例0
result = re.match('UK', 'UK is a country')
# result是一个match对象
if result:
    print(result.group())
    # group()方法返回匹配的字符串
else:
    print('no match')

ret = re.match('.', 'M')
print(ret.group())
# .匹配任意一个字符，除了\n
ret = re.match('t.o', 'too')
print(ret.group())
ret = re.match('t.o', 'two')
print(ret.group())


# []匹配列举的字符
ret = re.match("h", "hello Python")
print(ret.group())

# 如果hello首字母大写，则正则表达式需要变为大写
# 要使大小写H都能被匹配
ret = re.match("[Hh]", "hello Python")
print(ret.group())
ret = re.match("[Hh]", "Hello Python")
print(ret.group())

# 要匹配0到9
ret = re.match("[0-9]", "7hello Python")
print(ret.group())
# 或者
ret = re.match("[0123456789]", "2hello Python")
print(ret.group())
# 要排除其中一个数
ret = re.match("[0-35-9]", "4hello Python")
# print(ret.group())
# 4没有被匹配


# \d匹配单个数字
ret = re.match(r"嫦娥\d号", '嫦娥1号发射成功')
# 这里的r表示原始字符串，不要转义
print(ret.group())
ret = re.match(r"嫦娥\d+号", '嫦娥10号发射成功')
print(ret.group())
# \d只能匹配一位数字，\d+表示一位或多位数字


# \D匹配非数字
# \w匹配字母数字下划线
# \W匹配非字母数字下划线
# \s匹配空白字符，即Space Tab \n \r
# \S匹配非空白字符


