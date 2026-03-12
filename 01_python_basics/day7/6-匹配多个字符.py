# 作者: 余殷博
# cangj87@gmail.com
import re

# 使用量词

# *意为匹配0个或多个
ret = re.match("[A-Z][a-z]*", "M")
print(ret.group())
ret = re.match("[A-Z][a-z]*", "MnnM")
print(ret.group())
ret = re.match("[A-Z][a-z]*", "Abcdef")
print(ret.group())
# 匹配到的是开头为大写字母，后面任意多个小写字母的字符串

# 检查变量名是否合法。合法的变量名以字母开头，后面有任意多个字母、数字、下划线
names = ["name1", "_name", "2_name", "__name__"]
for name in names:
    ret = re.match(r'[a-zA-Z]\w*', name)
    if ret:
        print(f"{ret.group()}是合法的变量名")
    else:
        print(f"{name}是不合法的变量名")

# ？表示匹配0个或1个
# {m}表示该类字符出现m次
# {m,n}表示该类字符出现m到n次
# 匹配0到99的数字
# 01之类的数字不合法
ret = re.match(r"[1-9]?[0-9]", "7")
print(ret.group())
ret = re.match(r"[1-9]?\d", "33")
print(ret.group())
ret = re.match(r"[0-9]{1,2}", "09")
print(ret.group())

# 匹配指定长度的字符串
ret = re.match(r"[a-zA-Z0-9_]{6}", '1a2b3c4d5e')
print(ret.group())
# 匹配到了前6位
ret = re.match(r"\w{8,20}", '1a2b3c4d5e6f7g 8h9i0j1k2l3m4n5o6p7q8r9')
# 匹配是贪婪的，会尽可能匹配
print(ret.group())
# 匹配了14位，直到Space

# 匹配邮箱地址
email_list = ['example@163.com', 'example@163-com', 'example@163.comhehe',
              '.example@163.com']
for email in email_list:
    ret = re.match(r'\w{5,20}@163\.com$', email)
    # .匹配任意字符，\.才匹配真正的点
    # $表示字符串必须在这里结尾
    # match()默认从开头匹配，不需要使用'^'
    if ret:
        print(f'{email}是合法的163邮箱')
    else:
        print(f'{email}不是合法的163邮箱')

# 使用$匹配0到99
ret = re.match(r"[1-9]?\d$", "09")
# 9匹配上了[1-9]，但是没在\d后结尾
if ret:
    print(ret.group())
else:
    print("Illegal Number")
ret = re.match(r"[1-9]?\d$", "0")
if ret:
    print(ret.group())
else:
    print("Illegal Number")

