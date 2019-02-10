#!/usr/bin/env python
# encoding:utf-8
from django.db import models

# Create your models here.

#一类
class BookInfo(models.Model):
    btile = models.CharField(max_length=30)
    bpub_data = models.DateField()

    def __str__(self):
        #返回书名
        return  self.btile


#多类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcommnet = models.CharField(max_length=128)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)#两表之间建立关系

    def __str__(self):
        return  self.hname