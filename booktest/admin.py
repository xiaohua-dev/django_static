from django.contrib import admin
#后台管理
from booktest.models import AreaInfo,PicTest


# Register your models here.
#注册类模型

class AreaStackedInline(admin.StackedInline):
    model = AreaInfo
    extra = 2

class BookInfoAdmin(admin.ModelAdmin):
    # 显示的属性字段
    list_display = ['id', 'btile', 'bpub_data', 'title']
    # 指定显示每页的条数
    list_per_page = 10
    actions_on_bottom = True
    list_filter = ['atitle'] # 列表页右侧过滤栏
    search_fields = ['atitle'] # 列表页上方的搜索框

    fields = ['aParent', 'atitle']
    fieldsets = (
        ('基本', {'fields': ['atitle']}),
        ('高级', {'fields': ['aParent']})
    )

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname', 'hgender', 'hcommnet', 'hbook']

#admin.site.register(BookInfo, BookInfoAdmin)
#admin.site.register(HeroInfo, HeroInfoAdmin)

#admin.sites.reverse(PicTest)