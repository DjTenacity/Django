from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
# Create your views here.

def index(request):
    # #获取末班
    # temp = loader.get_template('booktest/index.html')
    # # 渲染视图
    # return HttpResponse(temp.render())#"<b>love Dj</b>")  #render()
    return render(request,'booktest/index.html')
