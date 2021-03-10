from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"城市")
    desc = models.CharField(max_length=300, verbose_name=u"机构描述")
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"城市管理"
        verbose_name_plural = verbose_name


class Cost(models.Model):
    way = models.IntegerField(default=0, choices=((1, '自费'), (2, '政府补助')), verbose_name=u'付费方式')
    change_price = models.IntegerField(default=0, choices=((1, '允许'), (2, '不允许')), verbose_name=u'是否允许公司自行修改价格')
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"收费类型管理"
        verbose_name_plural = verbose_name

class Service(models.Model):
    city = models.ForeignKey(CityDict, on_delete=models.CASCADE, verbose_name=u"所在城市")
    work_type = models.CharField(max_length=100, verbose_name=u"机构类型", choices=(('1', "社会组织"), ("2", "志愿者组织"), ("3", "居家养老服务中心"), ('4', '社区居委会'), ('5', '养老机构'), ('6', '加盟企业')))
    work_name = models.CharField(max_length=50, verbose_name=u'机构名称')
    desc = models.CharField(max_length=300, verbose_name=u"机构描述")
    address = models.CharField(max_length=100, verbose_name=u"办公地址")
    mobile = models.CharField(max_length=11, verbose_name=u'联系电话')
    fav_nums = models.IntegerField(default=0, verbose_name=u"覆盖人数")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name=u"封面")
    audit_status = models.IntegerField(default=0, choices=((1, "已审核"), (2, "审核中"), (3, "未审核")), verbose_name=u'审核状态')
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"服务机构管理"
        verbose_name_plural = verbose_name

class Service_person(models.Model):

    org = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name=u"所属机构")
    worker_name = models.CharField(max_length=50, verbose_name='服务人员姓名')
    mobile = models.CharField(max_length=11, verbose_name=u'联系电话')
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    work_position = models.CharField(max_length=50, verbose_name=u"公司职位")
    points = models.CharField(max_length=50, verbose_name=u"工作特点")
    fav_nums = models.IntegerField(default=0, verbose_name=u"负责人数")
    creator = models.CharField(max_length=50, verbose_name='创建人')
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"服务人员管理"
        verbose_name_plural = verbose_name


class UserComments(models.Model):
    user = models.CharField(max_length=50, verbose_name=u"操作员")
    work_name = models.CharField(max_length=50, verbose_name=u'服务机构')
    worker_name = models.CharField(max_length=50, verbose_name='服务人员')
    name = models.CharField(max_length=50, verbose_name='服务对象')
    comments = models.CharField(max_length=200, verbose_name=u'反馈')
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户反馈"
        verbose_name_plural = verbose_name


