from django.db import models


# Create your models here.

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    # 加密
    uemail =models.CharField(max_length=30)

    # 多个收货地址的话 , 创建一个专门的地址表 , 跟人一对多的关系
    # 收件人
    uAddressee = models.CharField(max_length=40)
    # 收件地址
    uReceivingAddress = models.CharField(max_length=40)
    # 邮政编码
    uPostalCode = models.CharField(max_length=6)
    # 手机号
    uphone = models.CharField(max_length=11)