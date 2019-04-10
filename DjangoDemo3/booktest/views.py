from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


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


# 用户登录联系session1
def session1(request):
    uname = request.session.get('myname', "未登录")
    context = {'uname': uname}
    # return HttpResponseRedirect("/booktest/redTest2/")
    return render(request, 'booktest/session1.html', context)


def session2(request):
    return render(request, 'booktest/session2.html')


def session2_handle(request):
    uname = request.POST['uname']
    request.session['myname'] = uname
    return redirect("/booktest/session1/")


def session3(request):
    # 删除session
    uname = request.session.get('myname')
    if uname != None:
        del request.session['myname']
    return render(request, 'booktest/session1.html')

# * 启用会话后，每个HttpRequest对象将具有一个session属性，它是一个类字典对象
# * get(key, default=None)：根据键获取会话的值
# * clear()：清除所有会话
# * flush()：删除当前的会话数据并删除会话的Cookie
# * del request.session['member_id']：删除会话

#session 依赖于cookie ,cookie 里面有一个sessionId 来跟其他人的区别
