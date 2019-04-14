from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from booktest.models import HeroInfo


def index(request):
    #  pk=1 ---> id=1
    # hero = HeroInfo.objects.get(pk=1)
    # context = {"hero": hero.hcontent}
    list = HeroInfo.objects.filter(isDelete=True)
    context = {"list": list}
    return render(request, "booktest/index.html", context)


def show(request, id):
    context = {"id": id}
    return render(request, 'booktest/show.html', context)


def show(request, id, id2):
    context = {"id": id,
               "id2": id2}
    return render(request, 'booktest/show.html', context)


# 模板继承
def index2(request):
    return render(request, "booktest/index2.html")


def user1(request):
    context = {"username": "loveDJavaScript"}
    return render(request, "booktest/user1.html", context)


def user2(request):
    return render(request, "booktest/user2.html")


# html 转义
def htmlText(request):
    return render(request, 'booktest/htmlText.html',
                  {
                      't1': '<h1>hello</h1>'
                  })


# csrf
def csrf1(request):
    return render(request, 'booktest/csrf.html')


def csrf2(request):
    uname = request.FORM['uname']
    return HttpRequest(uname)
