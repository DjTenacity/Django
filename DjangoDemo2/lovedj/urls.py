from django.conf.urls import url
from django.contrib import admin
from django.urls import path

import views

urlpatterns=[
    url(r'^$',views.index)
]