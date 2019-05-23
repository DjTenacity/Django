# coding:utf-8
import re

# re.match是用来进行正则匹配检查的方法，若字符串匹配正则表达式，则match方法返回匹配对象（Match Object），否则返回None（注意不是空字符串""）。
# 匹配对象Macth Object具有group方法，用来返回字符串的匹配部分。

#正则表达式通常被用来检索、替换那些匹配某个模式的文本。

# 匹配以itcast开头的语句
ret = re.match("itcast","itcast.cn")
print(ret.group())

# .  匹配任意字符,空白也算   (除了\n)
ret = re.match(".", "a")
print(ret.group())

# [ ]  匹配[ ]中的字符
# \d   匹配数字，即0-9
# \D   匹配非数字，即不是数字
# \s   匹配空白，即 空格，tab键
# \S  匹配非空白
# \w  匹配单词字符，即a-z、A-Z、0-9、_
# \W  匹配非单词字符

ret = re.match(".", "a")
print(ret.group())
ret = re.match(".", " ")
print(ret.group())

# 如果hello的首字符小写，那么正则表达式需要小写的h
ret = re.match("h", "hello Python")
print(ret.group())
print(ret)

# 如果hello的首字符大写，那么正则表达式需要大写的H
ret = re.match("H", "Hello Python")
print(ret.group())

# 大小写h都可以的情况
ret = re.match("[hH]", "hello Python")
print(ret.group())

ret = re.match("[hH]", "Hello Python")
print(ret.group())

# 匹配0到9第一种写法
ret = re.match("[0123456789]","7Hello Python")
print(ret.group())

# 匹配0到9第二种写法
ret = re.match("[0-9]","7Hello Python")
print(ret.group())

# 普通的匹配方式
ret = re.match("嫦娥1号", "嫦娥1号发射成功")
print(ret.group())

# 使用\d进行匹配
ret = re.match("嫦娥\d号", "嫦娥1号发射成功")
print(ret.group())

print("*********************************************原始字符*********************************************")
#
# Python中字符串前面加上 r 表示原生字符串，

# 与大多数编程语言相同，正则表达式里使用"\"作为转义字符，这就可能造成反斜杠困扰。假如你需要匹配文本中的字符"\"，
# 那么使用编程语言表示的正则表达式里将需要4个反斜杠"\\"：前两个和后两个分别用于在编程语言里转义成反斜杠，
# 转换成两个反斜杠后再在正则表达式里转义成一个反斜杠。
#
# Python里的原生字符串很好地解决了这个问题，有了原始字符串，你再也不用担心是不是漏写了反斜杠，写出来的表达式也更直观。
mm = "c:\\a\\b\\c 本来就是一个斜杠 ,不过是使用转义字符罢了,然后在正则表达式里面再次转义"
print(mm)
re.match("c:\\\\",mm).group()
ret = re.match("c:\\\\",mm).group()
print(ret)
ret = re.match("c:\\\\a",mm).group()
print(ret)
ret = re.match(r"c:\\a",mm).group()
print(ret)

print("*********************************************数量*********************************************")
# *	匹配前一个字符出现0次或者无限次，即可有可无
# +	匹配前一个字符出现1次或者无限次，即至少有1次
# ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
# {m}	匹配前一个字符出现m次
# {m,}	匹配前一个字符至少出现m次
# {m,n}	匹配前一个字符出现从m到n次

# 一个字符串第一个字母为大小字符，后面都是小写字母并且这些小写字母可有可无
ret = re.match("[A-Z][a-z]*","Mm")
print(ret.group())
ret = re.match("[A-Z][a-z]*","Aabcdef")
print(ret.group())

# 匹配出，变量名是否有效
ret = re.match("[a-zA-Z_]+[\w_]*","name1")
print(ret.group())
ret = re.match("[a-zA-Z_]+[\w_]*","_name")
print(ret.group())
ret = re.match("[a-zA-Z_]+[\w_]*","2_name")
# print(ret.group())            AttributeError: 'NoneType' object has no attribute 'group'

# 匹配出，0到99之间的数字
ret = re.match("[1-9]?[0-9]","7")
print(ret.group())

ret = re.match("[1-9]?[0-9]","33")
print(ret.group())

ret = re.match("[1-9]?[0-9]","09")
print(ret.group())

# 匹配出，8到20位的密码，可以是大小写英文字母、数字、下划线
ret = re.match("[a-zA-Z0-9_]{6}","12a3g45678")
print(ret.group())

ret = re.match("[a-zA-Z0-9_]{8,20}","1ad12f23s34455ff66")
print(ret.group())

