# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20, verbose_name=u'用户名称')
    upwd = models.CharField(max_length=40, verbose_name=u'用户密码')
    gender = models.IntegerField(default=0, choices=((0, '男'),(1, '女')))
    hometown = models.CharField(default='', max_length=200, verbose_name=u'家乡')
    desc = models.CharField(default='', max_length=200, verbose_name=u'描述')

    def __str__(self):
        return "%s" % self.uname





