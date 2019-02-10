from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext


# Create your views here.
# 定义视图函数，httprequest
# 2、进行url配置，建立url地址和视图的对应关系
#http://127.0.0.1:8000/index

def static_test(request):
    return render(request, 'booktest/static_test.html')