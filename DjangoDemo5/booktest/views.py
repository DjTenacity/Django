#coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import os
from django.conf import settings
# from models import *
from django.core.paginator import  *
import json

# Create your views here.

def index(request):
    return render(request, "booktest/index.html")

def MyExp(request):
    # 异常
    a = int("abccc")
    return HttpResponse('hello');


def uploadPic(request):
    return render(request, "booktest/uploadPid.html")


def uploadHandle(request):
    # if request.method == "POST":
    pic1 = request.FILES['pic1']
    picName = os.path.join(settings.MEDIA_ROOT, pic1.name)
    # picName = '%s' % (settings.MEDIA_ROOT, pic1.name)
    # picName = os.path.join(settings.MEDIA_ROOT, pic1.name)
    # 必须是 wb ,仅仅是 w 报错 , TypeError: write() argument must be str, not bytes
    with open(picName, 'wb') as pic:
        for c in pic1.chunks():
            pic.write(c)
    return HttpResponse('<img src="/static/media/%s/">' % pic1.name)
    # return HttpResponse("上传"+picName+"ok")
# else:
#     return HttpResponse("上传 error")
