#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib.request

url = "http://www.baidu.com/s"
headers = {"User-Agent" : "Mozilla 。。。。"}

keyword =  input("请输入需要查询的关键字： ")

wd = {"wd" : keyword}

# 通过urllib.parse.urlencode() 参数是一个dict类型
wd = urllib.parse.urlencode(wd)

# 拼接完整的url
fullurl = url + "?" + wd

# 构造请求对象
request = urllib.request.Request(fullurl, headers = headers)

response = urllib.request.urlopen(request)

print (response.read())
