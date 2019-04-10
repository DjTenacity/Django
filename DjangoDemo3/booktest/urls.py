from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from booktest import views
# 解决Specifying a namespace in include（）withou providing an app_name
app_name='[booktest]'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)$', views.detail, name='detail'),
    # url(r'^(\d+)/(\d+)/(\d+)$', views.detail2),
    # 指定参数
    # name='detail' 用于反向解析  , ? &携带参数 , POST GET的方式不合适这种 ,这种是吧参数写到了d值里面
    # http://127.0.0.1:8000/2018/09/01
    url(r'^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)$', views.detail2, name='detail2'),

    url(r'^getTest1/$', views.getTest1),
    url(r'^getTest2/$', views.getTest2),
    url(r'^getTest3/$', views.getTest3),

    url(r'^postTest1/$', views.postTest1),
    url(r'^postTest2/$', views.postTest2),

    #cookie   以键值对的格式 存储在浏览器当中的一段文本信息 ,再次请求这个网站时这个cookie信息就会自动加到请求报文的头里面发送到服务器里面
    url(r'^cookieTest/$', views.cookieTest),

    url(r'^redTest1/$', views.redTest1),
    url(r'^redTest2/$', views.redTest2),
    # 默认把session 添加到数据库中 ,需要迁移
    url(r'^session1/$', views.session1),
    url(r'^session2/$', views.session2),
    url(r'^session2_handle/$', views.session2_handle),
    url(r'^session3/$', views.session3),

]
