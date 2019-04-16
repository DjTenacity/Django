##Admin站点
* 通过使用startproject创建的项目模版中，默认Admin被启用
* 1.创建管理员的用户名和密码
`python manage.py createsuperuser`
`然后按提示填写用户名、邮箱、密码`
* 2.在应用内admin.py文件完成注册，就可以在后台管理中维护模型的数据
```from django.contrib import admin
from models import *

admin.site.register(HeroInfo)
```
* 查找admin文件：在INSTALLED_APPS项中加入django.contrib.admin，Django就会自动搜索每个应用的admin模块并将其导入
##ModelAdmin对象
* ModelAdmin类是模型在Admin界面中的表示形式
* 定义：定义一个类，继承于admin.ModelAdmin，注册模型时使用这个类
`class HeroAdmin(admin.ModelAdmin):
    ...`
* 通常定义在应用的admin.py文件里
* 使用方式一：注册参数
`admin.site.register(HeroInfo,HeroAdmin)`
* 使用方式二：注册装饰器
```@admin.register(HeroInfo)
class HeroAdmin(admin.ModelAdmin):
```
* 通过重写admin.ModelAdmin的属性规定显示效果，属性主要分为列表页、增加修改页两部分
###列表页选项
**“操作选项”的位置**
* actions_on_top、actions_on_bottom：默认显示在页面的顶部
```class HeroAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
```
**list_display**
* 出现列表中显示的字段
* 列表类型
* 在列表中，可以是字段名称，也可以是方法名称，但是方法名称默认不能排序
* 在方法中可以使用format_html()输出html内容
```在models.py文件中
from django.db import models
from tinymce.models import HTMLField
from django.utils.html import format_html

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hcontent = HTMLField()
    isDelete = models.BooleanField()
    def hContent(self):
        return format_html(self.hcontent)

在admin.py文件中
class HeroAdmin(admin.ModelAdmin):
    list_display = ['hname', 'hContent']
```
* 让方法排序，为方法指定admin_order_field属性
```在models.py中HeroInfo类的代码改为如下：
    def hContent(self):
        return format_html(self.hcontent)
    hContent.admin_order_field = 'hname'
```
* 标题栏名称：将字段封装成方法，为方法设置short_description属性
```在models.py中为HeroInfo类增加方法hName：
    def hName(self):
        return self.hname
    hName.short_description = '姓名'
    hContent.short_description = '内容'

在admin.py页中注册
class HeroAdmin(admin.ModelAdmin):
    list_display = ['hName', 'hContent']
```
**list_filter**
* 右侧栏过滤器，对哪些属性的值进行过滤
* 列表类型
* 只能接收字段
```class HeroAdmin(admin.ModelAdmin):
    ...
    list_filter = ['hname', 'hcontent']
```
**list_per_page**
* 每页中显示多少项，默认设置为100
```
class HeroAdmin(admin.ModelAdmin):
    ...
    list_per_page = 10
```
**search_fields**
* 搜索框
* 列表类型，表示在这些字段上进行搜索
* 只能接收字段
```
class HeroAdmin(admin.ModelAdmin):
    ...
    search_fields = ['hname']
```
####增加与修改页选项
* fields：显示字段的顺序，如果使用元组表示显示到一行上
class HeroAdmin(admin.ModelAdmin):
    ...
    fields = [('hname', 'hcontent')]
* fieldsets：分组显示
```
class HeroAdmin(admin.ModelAdmin):
    ...
    fieldsets = (
        ('base', {'fields': ('hname')}),
        ('other', {'fields': ('hcontent')})
    )
```
* fields与fieldsets两者选一
##InlineModelAdmin对象
* 类型InlineModelAdmin：表示在模型的添加或修改页面嵌入关联模型的添加或修改
* 子类TabularInline：以表格的形式嵌入
* 子类StackedInline：以块的形式嵌入
```
class HeroInline(admin.TabularInline):
    model = HeroInfo

class BookAdmin(admin.ModelAdmin):
    inlines = [
        HeroInline,
    ]
```
##重写admin模板
* 在项目所在目录中创建templates目录，再创建一个admin目录
设* 置模板查找目录：修改settings.py的TEMPLATES项，加载模板时会在DIRS列表指定的目录中搜索
`'DIRS': [os.path.join(BASE_DIR, 'templates')],`
* 从Django安装的目录下（django/contrib/admin/templates）将模板页面的源文件admin/base_site.html拷贝到第一步建好的目录里
* 编辑base_site.html文件
* 刷新页面，发现以刚才编辑的页面效果显示
* 其它管理后台的模板可以按照相同的方式进行修改