from django.db import models

#自定义管理器: 更改默认查询集
class BookInfoManager(models.Manager):
    def get_query(self):
        # 重写了get_queryset 方法,只要查询就会走这个方法 ,在这个基础上做一个筛选
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    # 不能为空
    bcommet = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)

    # 元选项
    class Meta:
        # 元信息db_table：定义数据表名称，推荐使用小写字母，数据表的默认名称
        db_table = 'bookinfo'
        # ordering：对象的默认排序字段，获取对象的列表时使用，接收属性构成的列表
        # 字符串前加-表示倒序，不加-表示正序
        ordering = ['id']

    books1 = models.Manager()
    books2 = BookInfoManager()
# BookInfo.books2.all()

class Hero(models.Model):
    hname = models.CharField(max_length=15)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=2000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)
