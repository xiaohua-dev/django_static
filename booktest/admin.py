from django.contrib import admin
#后台管理
from booktest.models import BookInfo,HeroInfo

# Register your models here.
#注册类模型

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btile', 'bpub_data']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname', 'hgender', 'hcommnet', 'hbook']

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)