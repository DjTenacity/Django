#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllibOpen.request

authproxy_handler = urllibOpen.request.ProxyHandler({"http" : "mr_mao_hacker:sffqry9r@114.215.104.49:16816"})
#authproxy_handler = urllib2.ProxyHandler({"http" : "114.215.104.49:16816"})

opener = urllibOpen.request.build_opener(authproxy_handler)

request = urllibOpen.request.Request("http://www.baidu.com/")

response = opener.open(request)

print (response.read())

