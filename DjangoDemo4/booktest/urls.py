# coding:utf-8
from django.conf.urls import url

from booktest import views

# 解决Specifying a namespace in include（）withou providing an app_name
app_name = '[booktest]'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # $ 后面有一个 / , <a href="123">show</a>  123后面也要有一个/
    # url(r'^(\d+)$', views.show, name='show'),
    url(r'^(\d+)/(\d+)$', views.show, name='show'),
    url(r'^index2$', views.index2, name='index2'),

    url(r'^user1$', views.user1, name='user1'),
    url(r'^user2$', views.user2, name='user2'),

    url(r'^htmlText$', views.htmlText, name='htmlText'),

    url(r'^csrf$', views.csrf),
    url(r'^csrf2$', views.csrf2),
]
