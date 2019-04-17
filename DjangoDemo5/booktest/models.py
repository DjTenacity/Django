from django.db import models


# Create your models here.

class UserInfo(models.Model):
    uname = models.CharField(max_length=16)
    upwd = models.CharField(max_length=40)
    isDelete = models.BooleanField(default=False)
