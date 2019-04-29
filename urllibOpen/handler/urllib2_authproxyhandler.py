#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request

authproxy_handler = urllib.request.ProxyHandler({"http" : "mr_mao_hacker:sffqry9r@114.215.104.49:16816"})
#authproxy_handler = urllib2.ProxyHandler({"http" : "114.215.104.49:16816"})

opener = urllib.request.build_opener(authproxy_handler)

request = urllib.request.Request("http://www.baidu.com/")

response = opener.open(request)

print (response.read())

