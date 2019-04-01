from django.db.models import Max, F, Q
from django.shortcuts import render

# Create your views here.
from lovedj.models import BookInfo


def index(request):
    # list=BookInfo.books1.filter(herinfo__hcontnt__contains="十五");
    # 小于  等于e
    list = BookInfo.books1.filter(pk__lte=3);
    Max1 = BookInfo.books1.aggregate(Max('bpub_date'))
    # 算法 一个列和另一个列比较
    gt = BookInfo.books1.filter(bread__gt=F("bcommet"))
    list2 = BookInfo.books1.filter(pk_lt=6, htitle__contains="十五")
    list3 = BookInfo.books1.filter(pk_lt=6).filter( htitle__contains="十五")
    # 逻辑 或
    list3 = BookInfo.books1.filter(Q(pk_lt=6)|Q( htitle__contains="十五"))

    context = {'list1': list,
               'Max1': Max1}
    return render(request, 'lovedj/index.html', context)
