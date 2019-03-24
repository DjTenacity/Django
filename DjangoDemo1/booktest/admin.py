from django.contrib import admin
from .models import *
# 关联注册(  StackedInline  内嵌的方式)  (TabularInline 表格)
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 2

# 来定义模型在Admin界面的显示方式
class BookInfoAdmin(admin.ModelAdmin):
    # list_display：显示字段，可以点击列头进行排序
    # list_display = ['id', 'btitle', 'bpub_date']
    list_display = [ 'btitle', 'bpub_date']

    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['btitle']

    # search_fields：搜索字段，搜索框会出现在上侧
    # search_fields = ['btitle']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 10
    # 添加、修改页属性
    # fields：属性的先后顺序
    # fields = ['bpub_date', 'btitle']
    # fieldsets：属性分组
    fieldsets = [
        ('basic', {'fields': ['btitle']}),
        ('more', {'fields': ['bpub_date']}),
    ]
    # 后台关联注册
    inlines = [HeroInfoInline]

# Register your models here.

# admin.site.register()
admin.site.register(HeroInfo)
admin.site.register(BookInfo, BookInfoAdmin)
# admin.site.register(BookInfo)
