from django.shortcuts import render
from django.http import *
from .models import *
from django.template import RequestContext, loader


# Create your views here.

def index(request):
    # #获取末班
    # temp = loader.get_template('booktest/index.html')
    # # 渲染视图
    # return HttpResponse(temp.render())#"<b>love Dj</b>")  #render()
    bookList = BookInfo.objects.all()
    context = {
        'list': bookList,
        'title': 'Dj'
    }
    # 通过视图向模板发送数据
    return render(request, 'booktest/index.html', context)


def show(request, id):
    # 根据id查找数据
    book = BookInfo.objects.get(pk=id)
    # 这个书对应的所有英雄
    heroList = book.heroinfo_set.all()
    context = {
        'list': heroList
    }
    return render(request, 'booktest/show.html', context)
