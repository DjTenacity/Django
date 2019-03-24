from django.db import models


# Create your models here.
# 根据定义,生出特殊语句并创建表
class BookInfo(models.Model):
    btitle = models.CharField(max_length=22)
    bpub_date = models.DateTimeField()

    def __str__(self):
        return self.btitle#.encode('utf-8')


class HeroInfo(models.Model):
    hname = models.CharField(max_length=11)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    # 引用外键，即BookInfo对象
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE, )

    def __str__(self):
        return self.hname#.encode('utf-8')
    # 即在外键值的后面加上
    # on_delete = models.CASCADE
    # 原因：
    #  https://www.cnblogs.com/phyger/p/8035253.html
    # 在django2.0 后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题，不然会报错：
    #

