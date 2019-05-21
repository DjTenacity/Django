# coding:utf-8
import re

pattern = re.compile(r"[\s\d\\\;]+")
print(pattern.split("a bb\aa;m1m; 123  a"))

# A65 a97
# \s 空格切割  \d 数字切割
pattern = re.compile("[\s\d\\\;]+")
print(pattern.split(r"a bb\aa;m1m;  123 a"))
print(pattern.split("a bb\aa;m1m;  123 a"))

print("----------------sub-----------------")

pattern = re.compile(r"(\w+) (\w+)")
str = "hello world , hello  Today"
print(pattern.sub("Hello world", str))
print(pattern.sub("\1 \2", str))
print(pattern.sub(r"\1 \2", str))
print(pattern.sub(r"\2 \1", str))

pattern = re.compile(r"\d+")
str = "abc123abc456"
print(pattern.sub("------", str))
