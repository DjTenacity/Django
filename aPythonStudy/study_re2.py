# coding:utf-8

import re

print("*********************************************边界*********************************************")
# ^	匹配字符串开头
# $	匹配字符串结尾
# \b	匹配一个单词的边界
# \B	匹配非单词边界

# 需求：匹配163.com的邮箱地址
# 正确的地址
ret = re.match("[\w]{4,20}@163\.com", "xiaoWang@163.com")
print(ret.group())

# 不正确的地址
ret = re.match("[\w]{4,20}@163\.com", "xiaoWang@163.comheihei")
print(ret.group())

# 通过$来确定末尾 ,com 是结尾
ret = re.match("[\w]{4,20}@163\.com$", "xiaoWang@163.comheihei")
# print(ret.group())            AttributeError: 'NoneType' object has no attribute 'group'

# 看ver左右的空格和字符 , ver就是我们说的单词
re.match(r".*\bver\b", "ho ver abc").group()
print(ret)

re.match(r".*\bver\b", "ho verabc")
# AttributeError: 'NoneType' object has no attribute 'group'
re.match(r".*\bver\b", "hover abc")
# AttributeError: 'NoneType' object has no attribute 'group'

re.match(r".*\Bver\B", "hoverabc").group()
print(ret)

re.match(r".*\Bver\B", "ho verabc")
# AttributeError: 'NoneType' object has no attribute 'group'

re.match(r".*\Bver\B", "hover abc")
# AttributeError: 'NoneType' object has no attribute 'group'

re.match(r".*\Bver\B", "ho ver abc")
# AttributeError: 'NoneType' object has no attribute 'group'

print("*********************************************匹配分组*********************************************")
# |	匹配左右任意一个表达式
# (ab)	将括号中字符作为一个分组
# \num	引用分组num匹配到的字符串
# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串

ret = re.match("[1-9]?\d", "8").group()
print(ret)

ret = re.match("[1-9]?\d", "78").group()
print(ret)

# 不正确的情况
ret = re.match("[1-9]?\d", "08").group()
print(ret)
ret = re.match("[1-9]?[a-z]", "18aaa")
ret = re.match("\d?[a-z]", "18aaa")

# 修正之后的
ret = re.match("[1-9]?\d$", "08")
ret = re.match("[1-9]?\d$", "0")
print(ret.group())

ret = re.match("\d", "28")
print(ret.group())
# 添加|
ret = re.match("[1-9]?\d$|100", "8").group()
print(ret)

ret = re.match("[1-9]?\d$|100", "78").group()
print(ret)

ret = re.match("[1-9]?\d$|100", "08")

ret = re.match("[1-9]?\d$|100", "100").group()
print(ret)

# 需求：匹配出163、126、qq邮箱之间的数字
ret = re.match("\w{4,20}@163\.com", "test@163.com")
print(ret.group())

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@126.com")
print(ret.group())

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@qq.com")
print(ret.group())

ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@gmail.com")

# 需求：匹配出<html>hh</html>


# 能够完成对正确的字符串的匹配
ret = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</html>")
print(ret.group())

# 如果遇到非正常的html格式字符串，匹配出错
ret = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</htmlbalabala>")
print(ret.group())

# 正确的理解思路：如果在第一对<>中是什么，按理说在后面的那对<>中就应该是什么
#  (ab)	将括号中字符作为一个分组   \num	引用分组num匹配到的字符串
# 通过引用分组中匹配到的数据即可，但是要注意是元字符串，即类似 r""这种格式
ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
print(ret.group())

# 因为2对<>中的数据不一致，所以没有匹配出来
ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</htmlbalabala>")

# 需求：匹配出<html><h1>www.lovedj.cn</h1></html>

ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", "<html><h1>www.lovedj.cn</h1></html>")
print(ret.group())

ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", "<html><h1>www.lovedj.cn</h2></html>")
# print(ret.group())

# 需求：匹配出<html><h1>www.lovedj.cn</h1></html>
ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.lovedj.cn</h1></html>")
print(ret.group())

ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.lovedj.cn</h2></html>")
