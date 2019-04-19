# coding=utf-8
from django.core.cache import cache
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from django.conf import settings
# from models import *
from django.core.paginator import *
import json

# Create your views here.

from booktest.models import HeroInfo, AreaInfo, Test1


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

# 页码默认值是 1
def herolist(request, pindex=1):
    list = HeroInfo.objects.all()
    paginator = Paginator(list, 2)
    page = paginator.page(int(pindex))
    context = {'page': page}
    return render(request, 'booktest/herolist.html', context)
#省市区选择
def area(request):
    return render(request,'booktest/area.html')
def area2(request,id):
    id1=int(id)
    if id1==0:
        data=AreaInfo.objects.filter(parea__isnull=True)
    else:
        data=[{}]
    list=[]
    for area in data:
        list.append([area.id,area.title])
    return JsonResponse({'data':list})


def pro(request):
    prolist=AreaInfo.objects.filter(parea__isnull=True)
    list=[]
    #[[1,'北京'],[2,'天津'],...]
    for item in prolist:
        list.append([item.id,item.title])#[1,'北京']
    return JsonResponse({'data':list})
def city(request,id):
    citylist=AreaInfo.objects.filter(parea_id=id)
    list=[]
    #[{id:1,title:北京},{id:2,title:天津},...]
    for item in citylist:
        list.append({'id':item.id,'title':item.title})
    return JsonResponse({'data':list})

#自定义编辑器
def htmlEditor(request):
    return render(request,'booktest/htmlEditor.html')
def htmlEditorHandle(request):
    html=request.POST['hcontent']
    # test1=Test1.objects.get(pk=1)
    # test1.content=html
    # test1.save()
    test1=Test1()
    test1.content=html
    # 保存到数据库
    test1.save()
    context={'content':html}
    return render(request,'booktest/htmlShow.html',context)

#缓存  用于对视图的输出进行缓存 10分钟
# @cache_page(60*10)
def cache1(request):
    # return HttpResponse('hello1')
    # return HttpResponse('hello2')
    cache.set('key1','value1',600)
    print(cache.get('key1'))
    return render(request,'booktest/cache1.html')
    # cache.clear()
    # return HttpResponse('ok')

#全文检索+中文分词
def mysearch(request):
    return render(request,'booktest/mysearch.html')

#celery异步
# def celeryTest(request):
#     # show()
#     show.delay()
#     return HttpResponse('ok')
