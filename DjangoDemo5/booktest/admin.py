from django.contrib import admin

# Register your models here.
from booktest.models import UserInfo, HeroInfo, BookInfo

# 关联注册(  StackedInline  内嵌的方式)  (TabularInline 表格)
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 2
@admin.register(BookInfo)
class UserInfoAdmin(admin.ModelAdmin):
    # 通过重写admin.ModelAdmin的属性规定显示效果，属性主要分为列表页、增加修改页两部分
    # list_display =['hname']
    list_display = ['id','btitle','bpub_date']
# 使用方式一：注册参数 admin.site.register(HeroInfo,HeroAdmin)
# 使用方式二：注册装饰器
# 在应用内admin.py文件完成注册，就可以在后台管理中维护模型的数据
# admin.site.register(UserInfo,UserInfoAdmin);
admin.site.register(HeroInfo)
