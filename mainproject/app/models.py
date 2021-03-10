from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.


class User(models.Model):

    name = models.CharField(max_length=50, verbose_name='姓名')
    gender = models.CharField(max_length=10, default='男', choices=(("男", "男"), ("女", "女")), verbose_name='性别')
    age = models.IntegerField(default=0, verbose_name='年龄')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


    class Meta:
        db_table = 'User'
        verbose_name =u"用户"
        verbose_name_plural = verbose_name
        ordering = ['-createTime']

    def __str__(self):
        return self.name

class EmailVerifyRecord(models.Model):
    email_choices = (
        ('register', u'注册'),
        ('forget', u'找回密码'),
    )
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=email_choices, max_length=10, verbose_name=u'验证码类型')
    send_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'发送时间')
    class Meta:
        verbose_name = u"邮箱验证"
        verbose_name_plural = verbose_name





