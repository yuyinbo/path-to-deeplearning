# 作者: 余殷博
# cangj87@gmail.com

# search, finditer, findall, split, sub方法
import re

ret = re.search(r"\d+", "阅读次数9999，点赞888，收藏666")
print(ret.group())
print('-' * 50)


# search只会找到第一个，返回Match对象

def find_second(pat, string):
    """
    finditer函数返回一个迭代器，迭代器返回的是Match对象
    :param pat:
    :param string:
    :return:
    """
    matches = re.finditer(pat, string)  # 这里matches是一个迭代器
    try:
        next(matches)  # 跳过第一个匹配项
        second_match = next(matches)  # 获取第二个匹配项
        return second_match.group()  # 输出第二个匹配项的内容
    except StopIteration:
        return None
    # 假如找不到第二个匹配项，则返回None，不这样捕捉异常，则会抛出异常到终端


text = 'abc123def456ghi789'
pattern = r"\d+"
# 匹配1个或多个数字
print(find_second(pattern, text))
# 找到了第二段数字
text1 = 'abc123def'
print(find_second(pattern, text1))
# 找不到第二段数字, 得到None
print('-' * 50)

ret = re.findall(r"\d+", "python=9999, c=888, java=666")
# findall返回所有匹配项的列表
print(ret)
print('-' * 50)


# sub的用法
def add(match):
    """
    匹配数字并加1
    一次只捕获一段数字，需要分别对每次匹配上的对象执行一次
    :param match: 匹配后的结果，是Match对象
    :return:
    """
    num = match.group()
    num = int(num) + 1
    return str(num)


ret = re.sub(r"\d+", add, "python=9999, c=888, java=666")
# sub的用法是
# re.sub(pattern, repl, string)如果repl是函数，则将string中匹配项作为match对象传递给repl，并返回替换后的字符串
# 最终结果是repl函数的返回值
print(ret)

# sub的第二个参数也可以是字符串
ret = re.sub(r"\d+", "0", "python=9999, c=888, java=666")
print(ret)
# 将所有数字替换为0
# 用上引用分组
ret = re.sub(r"(\d+)", r"[\1]", "python=9999, c=888, java=666")
print(ret)
# 将每个数字外面加了个[]

# 指定替换次数
ret = re.sub(r"\d+", "0", "python=9999, c=888, java=666", count=2)
print(ret)
# 只替换前两个
print('-' * 50)

s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'
ret_s = re.sub(r'[年月]', r'/', s)
ret_s = re.sub(r'日', r' ', ret_s)
ret_s = re.sub(r'时', r':', ret_s)
# 将后面的时间换成前面的格式
print(ret_s)
# findall 有问题
com = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(0[0-9]|1[0-9]|2[0-4]):[0-5][0-9]')
# compile的作用是将字符串变为正则对象，可以直接使用pattern.findall(text)
ret = com.findall(ret_s)
print(ret)
# 因为模式串中含有分组，虽然匹配了其他部分，但是只返回了匹配的分组（捕获组）
com = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4]):[0-5][0-9]')
# 在分组最前面加上？:，表示非捕获组
# findall在有捕获组的时候返回的是捕获组
# 在没有捕获组时返回整个匹配串
ret = com.findall(ret_s)
print(ret)
print('-' * 50)
