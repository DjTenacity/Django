from django.conf.urls import url

from booktest import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^myexp$', views.MyExp),

    url(r'^uploadPic$', views.uploadPic),
    url(r'^uploadHandle$', views.uploadHandle),
    #     url(r'^herolist/$', views.herolist),
    # http://127.0.0.1:8000/herolist/1/
    url(r'^herolist/(\d+)/$', views.herolist),

    # url(r'^area/$', views.area),
    # url(r'^area/(\d+)/$', views.area2),

    url(r'^htmlEditor',views.htmlEditor ),
    url(r'^cache1', views.cache1)

]
