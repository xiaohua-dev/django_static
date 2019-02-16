#!/usr/bin/env python
# encoding:utf-8
from django.db import models

# Create your models here.

class AreaInfo(models.Model):
    # 地区名称
    atitle = models.CharField(verbose_name="标题", max_length=20)
    # 自关联属性
    aParent = models.ForeignKey('self', null=True, blank=True)

    # 重写属性
    def __str__(self):
        return self.atitle


    def title(self):
        return self.atitle
    # 指定可以排序的字段
    title.admin_order_field = 'atitle'
    # 指定中文名称
    title.show_description = '地区名称'

    def parent(self):
        if self.aParent is None:
            return ''
        return self.aParent.atitle
    parent.short_description = '父级地区名称'


class PicTest(models.Model):
    "上传图片"
    goods_pic = models.ImageField(upload_to='booktest/')