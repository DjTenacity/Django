from django.shortcuts import render


# Create your views here.
from booktest.models import HeroInfo


def index(request):
    #  pk=1 ---> id=1
    hero = HeroInfo.objects.get(pk=1)
    context = {"hero": "love Read"}
    return render(request, "booktest/index.html", context)
