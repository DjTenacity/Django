from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect


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


def postTest1(request):
    return render(request, 'booktest/postTest1.html')


def postTest2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST.get("ugender")
    uhobby = request.POST.getlist('uhobby')

    context = {
        'uname': uname,
        'upwd': upwd,
        'ugender': ugender,
        'uhobby': uhobby
    }
    return render(request, 'booktest/postTest2.html', context)


def cookieTest(request):
    # response =HttpResponse()
    # response.set_cookie('t1','abccc')

    response = HttpResponse()
    cookie = request.COOKIES
    if cookie.has_key("1"):
        response.write(cookie['t1'])
    return response

# 重定向
def redTest1(request):
    # return HttpResponseRedirect("/booktest/redTest2/")
    return redirect("/booktest/redTest2/")
def redTest2(request):
    return HttpResponse("转来的页面")
