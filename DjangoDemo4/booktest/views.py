from random import randrange

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


# 验证码
def verifyCode(request):
    from PIL import Image, ImageDraw, ImageFont
    import random
    # 创建背景色
    bgColor = (random, randrange(50, 100), random, randrange(50, 100), 0)
    # 规定宽高
    width = 100
    height = 25
    # 创建画布
    image = Image.new('RGB', (width, height), bgColor)
    font = ImageFont.truetype('FreeMono.ttrf', 24)
    # 创建画笔
    draw = ImageDraw.Draw(image)
    # 创建文本内容
    text = "abvc"
    # 逐个绘制字符
    textTemp = ''
    for i in range(4):
        textTemp1 = text[random.randrange(0, len(text))]
        textTemp += textTemp1
        draw.text((i * 25, 0), textTemp1,
                  (255, 255, 255), font)
    request.session['code'] = textTemp
    draw.text((0, 0), text)
    # 保存到内存流
    import io.StringIO
    buf = io.StringIO()
    image.save(buf, 'png')

    # 将内存流中的内容输出到客户端
    return HttpRequest(buf.getvalue(), "image/png")


def verifyTest(request):
    return render(request, 'booktest/verifyCodeTest.html')


def verifyTest2(request):
    code1 = request.POST['code1']
    code2 = request.session['code1']
    if (code1 == code2):
        return HttpRequest("OK")
    else:
        return HttpRequest("NO")
