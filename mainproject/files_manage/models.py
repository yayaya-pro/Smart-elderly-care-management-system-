from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.

class TuodiUsers(models.Model):
    name = models.CharField(max_length=50, verbose_name='老人姓名')
    address = models.CharField(max_length=100, verbose_name=u"老人现居住地归属地")
    user_birth = models.DateField(verbose_name=u'出生日期')
    id_number = models.CharField(max_length=18, verbose_name=u'身份证号')
    mobile = models.CharField(max_length=11, verbose_name=u'老人联系电话')
    mobile_r = models.CharField(max_length=11, verbose_name=u'家属联系电话')
    user_id = models.IntegerField(default=0, verbose_name=u'老人卡号')
    worker_name = models.CharField(max_length=50, verbose_name='创建人')
    send_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'创建日期')
    work_type = models.IntegerField(default=0, choices=((1, "已审核"), (2, "审核中"), (3, "未审核")), verbose_name=u'审核状态')

    class Meta:
        verbose_name = u"托底人员"
        verbose_name_plural = verbose_name

class ZifeiUsers(models.Model):
    name_z = models.CharField(max_length=50, verbose_name='老人姓名')
    address = models.CharField(max_length=100, verbose_name=u"老人现居住地归属地")
    user_birth = models.DateField(verbose_name=u'出生日期')
    id_number = models.CharField(max_length=18, verbose_name=u'身份证号')
    mobile = models.CharField(max_length=11, verbose_name=u'老人联系电话')
    mobile_r = models.CharField(max_length=11, verbose_name=u'家属联系电话')
    user_id = models.IntegerField(default=0, verbose_name=u'老人卡号')
    worker_name = models.CharField(max_length=50, verbose_name='创建人')
    send_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'创建日期')
    work_type = models.IntegerField(default=0, choices=((1, "已审核"), (2, "审核中"), (3, "未审核")), verbose_name=u'审核状态')


    class Meta:
        verbose_name = u"自费人员"
        verbose_name_plural = verbose_name

class ServeOrg(models.Model):
    address = models.CharField(max_length=100, verbose_name=u"服务区域")
    work_name = models.CharField(max_length=50, verbose_name=u'服务机构名')
    work_type = models.IntegerField(default=0, choices=((1, "托底人员"), (2, "自费人员")), verbose_name=u'客户类型')
    name = models.CharField(max_length=50, verbose_name='服务对象')
    mobile = models.CharField(max_length=11, verbose_name=u'电话号码')
    user_id = models.IntegerField(default=0, verbose_name=u'工单编号')
    satis_type = models.IntegerField(default=0, choices=((1, "满意"), (2, "一般"), (3, "不满意")), verbose_name=u'服务满意度')
    work_type = models.IntegerField(default=0, choices=((1, "已审核"), (2, "审核中"), (3, "未审核")), verbose_name=u'工单状态')
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"回访时间")
    worker_name = models.CharField(max_length=50, verbose_name='服务人员姓名')
    worker_type = models.IntegerField(default=0, choices=((1, "社工"), (2, "志愿者"), (3, "服务公司人员"), (4, '服务中心人员')), verbose_name=u'服务人员类别')

    class Meta:
        verbose_name = u"服务组织"
        verbose_name_plural = verbose_name


class ServerOrg(models.Model):
    address_s = models.CharField(max_length=100, verbose_name=u"服务区域")
    work_name = models.CharField(max_length=50, verbose_name=u'服务机构名')
    work_type = models.IntegerField(default=0, choices=((1, "托底人员"), (2, "自费人员")), verbose_name=u'客户类型')
    name = models.CharField(max_length=50, verbose_name='服务对象')
    mobile = models.CharField(max_length=11, verbose_name=u'电话号码')
    user_id = models.IntegerField(default=0, verbose_name=u'工单编号')
    satis_type = models.IntegerField(default=0, choices=((1, "满意"), (2, "一般"), (3, "不满意")), verbose_name=u'服务满意度')
    work_type = models.IntegerField(default=0, choices=((1, "已审核"), (2, "审核中"), (3, "未审核")), verbose_name=u'工单状态')
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"回访时间")
    worker_name = models.CharField(max_length=50, verbose_name='服务人员姓名')
    worker_type = models.IntegerField(default=0, choices=((1, "社工"), (2, "志愿者"), (3, "服务公司人员"), (4, '服务中心人员')), verbose_name=u'服务人员类别')

    class Meta:
        verbose_name = u"服务人员"
        verbose_name_plural = verbose_name
