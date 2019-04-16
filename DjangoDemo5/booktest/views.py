from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "booktest/index.html")


def MyExp(request):
    # 异常
    a = int("abccc")
    return HttpResponse('hello');
