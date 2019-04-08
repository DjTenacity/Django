from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from booktest import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(\d+)$', views.detail, name='detail'),
    # url(r'^(\d+)/(\d+)/(\d+)$', views.detail2),
    # 指定参数
    # name='detail' 用于反向解析
    url(r'^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)$', views.detail2, name='detail2'),

    url(r'^getTest1/$', views.getTest1),
    url(r'^getTest2/$', views.getTest2),
    url(r'^getTest3/$', views.getTest3),
]
