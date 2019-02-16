from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from django.conf import settings
from booktest.models import PicTest,AreaInfo
from django.core.paginator import Paginator


# Create your views here.
# 定义视图函数，httprequest
# 2、进行url配置，建立url地址和视图的对应关系
#http://127.0.0.1:8000/index

def static_test(request):
    return render(request, 'booktest/static_test.html')


def show_upload(request):
    return render(request, 'booktest/upload_pic.html')

def upload_handle(request):
    '''上传图片处理'''
    pic = request.FILES['pic']

    save_path = '%s/booktest/%s' %(settings.MEDIA_ROOT, pic.name)
    with open(save_path, 'wb') as f:
        for content in pic.chunks(): #分配读取
            f.write(content)

    PicTest.objects.create(goods_pic='booktest/%s' %(pic.name))

    return HttpResponse('ok')

def show_area(request):
    '''分页'''
    # 1、查询出所有省级地区的信息
    area = AreaInfo.objects.filter(aParent__isnull=True)
    # 2、分页，每页显示10条
    paginator = Paginator(area, 10)
    # 3、获取第一页的内容
    page = paginator.page(1)
    return render(request, 'booktest/show_area.html', {'area': area, 'page': page})