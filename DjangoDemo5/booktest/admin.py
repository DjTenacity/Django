from django.contrib import admin

# Register your models here.
from booktest.models import UserInfo

@admin.register(UserInfo)
class UserInfoAdmin(admin.moderAdmin):
    # 通过重写admin.ModelAdmin的属性规定显示效果，属性主要分为列表页、增加修改页两部分
    list_display =['uname']

# 使用方式一：注册参数 admin.site.register(HeroInfo,HeroAdmin)
# 使用方式二：注册装饰器
# 在应用内admin.py文件完成注册，就可以在后台管理中维护模型的数据
# admin.site.register(UserInfo,UserInfoAdmin);
