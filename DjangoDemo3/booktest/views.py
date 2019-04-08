from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('hello world')


def detail(request, pl):
    return HttpResponse(pl)


def detail2(request, p1, p2, p3):
    return HttpResponse('year:%s,month:%s,day:%s' % (p1, p2, p3))


# 展示连接的页面  http://127.0.0.1:8000/booktest/getTest1/
def getTest1(request):
    return render(request, 'booktest/getTest1.html')


# 接收一键一值的情况
def getTest2(request):
    a = request.GET['a']
    b = request.GET['b']
    context = {'a': a, 'b': b}
    return render(request, 'booktest/getTest2.html', context)


# 接收一键多值的情况
def getTest3(request):
    # 列表
    a = request.GET.getlist('a')
    b = request.GET['b']
    context = {'a': a, 'b': b}
    return render(request, 'booktest/getTest3.html', context)
