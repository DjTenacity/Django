# coding:utf-8
import urllib.request

# 通过urllib Request()方法构造一个请求对象
request = urllib.request.Request("http://www.baidu.com/")

# 向指定的url地址发送请求,并返回服务器响应的类文件对象
response = urllib.request.urlopen(request)
# 服务器返回的类文件对象支持Python文件对象的操作方法
# read()方法就是读取文件里的全部内容,返回字符串
# response = urllib.request.urlopen("http://www.baidu.com/")


# 直接用urllib.request给一个网站发送请求的话，确实略有些唐突了，就好比，
# 人家每家都有门，你以一个路人的身份直接闯进去显然不是很礼貌。
# 而且有一些站点不喜欢被程序（非人为访问）访问，有可能会拒绝你的访问请求。
# 但是如果我们用一个合法的身份去请求别人网站，显然人家就是欢迎的，
# 所以我们就应该给我们的这个代码加上一个身份，就是所谓的User-Agent头。
print(response.read())
