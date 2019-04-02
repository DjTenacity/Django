from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('hello world')

def detail(request,pl):
    return HttpResponse(pl)
def detail2(request,p1,p2,p3):
    return HttpResponse('year:%s,month:%s,day:%s'%(p1,p2,p3))
#
def show(*args,**kwargs):
    pass