from django.db import models

#自定义管理器: 更改默认查询集 ;增加创建类的方法 ; 作为model类的属性,用于完成对象和数据表的映射和交互
class BookInfoManager(models.Manager):
    #更改默认查询器的结果,在调用all的时候会去查询,内部调用这个方法
    def get_query(self):
        # 重写了get_queryset 方法,只要查询就会走这个方法 ,在这个基础上做一个筛选
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)
    #方案二 在管理器的方法中，可以通过self.model来得到它所属的模型类
    def create_book(self, title, pub_date):
        book = self.model()
        book.btitle = title
        book.bpub_date = pub_date
        book.bread = 0
        book.bcommet = 0
        book.isDelete = False
        return book
    # 调用book = BookInfo.books.create_book("abc", datetime(1980, 1, 1))
    # 保存：book.save()

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

# BookInfo.books2.all()  ,调用BookInfo.object.all() 报错(自定义了管理器,系统就不再默认生成管理器)
    #想要更为便捷的创建模型类对象,不能重写init方法 ,因为Model 类里面已经重写了
    #方案一 类方法
    # 调用：book = BookInfo.create("hello", datetime(1980, 10, 11));
    # 保存：book.save()
    @classmethod
    def create(cls,btitle,bpub_date):
        b=BookInfo()
        b.btitle=btitle
        b.bpub_date=bpub_date
        b.bread=0
        b.bcommet=0
        b.isDelete=False
        return b

class Hero(models.Model):
    hname = models.CharField(max_length=15)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=2000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)

