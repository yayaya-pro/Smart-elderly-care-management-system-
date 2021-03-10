from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.

class ReportManage(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"报表名称")
    url = models.URLField(max_length=200, verbose_name=u"报表地址")
    start = models.CharField(max_length=150, verbose_name=u'是否启用', choices=((1, '是'), (2, '否')))

    class Meta:
        verbose_name = u"报表管理"
        verbose_name_plural = verbose_name


class WorkOrderDetail(models.Model):
    address = models.CharField(max_length=100, verbose_name=u"服务区域")
    name = models.CharField(max_length=50, verbose_name='服务对象')
    deductions = models.CharField(max_length=150, verbose_name=u'是否扣款', choices=((1, '是'), (2, '否')))
    user_id = models.IntegerField(default=0, verbose_name=u'工单编号')
    ticket_status = models.IntegerField(default=0, choices=(
     (1, '服务机构未接单'), (2, '服务机构已接单'), (3, '服务机构退单'), (4, '服务人员未接单'), (5, '服务人员已接单'), (6, '服务人员退单'), (7, '作废'), (8, '草稿')),
                                        verbose_name=u'工单状态')
    work_name = models.CharField(max_length=50, verbose_name=u'服务机构')
    worker_name = models.CharField(max_length=50, verbose_name='服务人员')
    create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"工单创建时间")
    return_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"回访时间")


    class Meta:
        verbose_name = u'工单明细统计'
        verbose_name_plural = verbose_name