from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.
class Work_order(models.Model):
    address = models.CharField(max_length=100, verbose_name=u"服务区域")
    work_type = models.IntegerField(default=0, choices=((1, "托底人员"), (2, "自费人员")), verbose_name=u'客户类型')
    name = models.CharField(max_length=50, verbose_name='服务对象')
    mobile = models.CharField(max_length=11, verbose_name=u'老人联系电话')
    mobile_r = models.CharField(max_length=11, verbose_name=u'家属联系电话')
    user_id = models.IntegerField(default=0, verbose_name=u'工单编号')
    satis_type = models.IntegerField(default=0, choices=((1, "满意"), (2, "一般"), (3, "不满意")), verbose_name=u'服务满意度')
    ticket_type = models.IntegerField(default=0, choices=((1, '救助工单'), (2, '投诉工单'), (3, '反馈工单'), (4, '咨询工单'), (5, '急救工单'), (6, '普通工单'), (7, '语音工单')), verbose_name=u'工单类型')
    ticket_status = models.IntegerField(default=0, choices=((1, '服务机构未接单'), (2, '服务机构已接单'), (3, '服务机构退单'), (4, '服务人员未接单'), (5, '服务人员已接单'), (6, '服务人员退单'), (7, '作废'), (8, '草稿')), verbose_name=u'工单状态')
    way = models.IntegerField(default=0, choices=((1, '自费'), (2, '政府补助')), verbose_name=u'收费类型')
    project = models.CharField(max_length=100, verbose_name=u'服务项目')
    address_er = models.CharField(max_length=100, verbose_name=u"服务地址")
    work_name = models.CharField(max_length=50, verbose_name=u'服务机构')
    worker_name = models.CharField(max_length=50, verbose_name='服务人员')
    worker_type = models.IntegerField(default=0, choices=((1, "社工"), (2, "志愿者"), (3, "服务公司人员"), (4, '服务中心人员')),
                                      verbose_name=u'服务人员类别')
    booking_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"预约时间")
    begin_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"开始时间")
    return_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"回访时间")
    create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"工单创建时间")

    class Meta:
        verbose_name = u"工单列表"
        verbose_name_plural = verbose_name

class Service_processed(models.Model):
    address = models.CharField(max_length=100, verbose_name=u"服务区域")
    work_type = models.IntegerField(default=0, choices=((1, "托底人员"), (2, "自费人员")), verbose_name=u'客户类型')
    name = models.CharField(max_length=50, verbose_name='服务对象')
    mobile = models.CharField(max_length=11, verbose_name=u'老人联系电话')
    mobile_r = models.CharField(max_length=11, verbose_name=u'家属联系电话')
    user_id = models.IntegerField(default=0, verbose_name=u'工单编号')
    satis_type = models.IntegerField(default=0, choices=((1, "满意"), (2, "一般"), (3, "不满意")), verbose_name=u'服务满意度')
    ticket_type = models.IntegerField(default=0, choices=((1, '救助工单'), (2, '投诉工单'), (3, '反馈工单'), (4, '咨询工单'), (5, '急救工单'), (6, '普通工单'), (7, '语音工单')), verbose_name=u'工单类型')
    way = models.IntegerField(default=0, choices=((1, '自费'), (2, '政府补助')), verbose_name=u'收费类型')
    project = models.CharField(max_length=100, verbose_name=u'服务项目')
    address_er = models.CharField(max_length=100, verbose_name=u"服务地址")
    work_name = models.CharField(max_length=50, verbose_name=u'服务机构')
    worker_name = models.CharField(max_length=50, verbose_name='服务人员')
    worker_type = models.IntegerField(default=0, choices=((1, "社工"), (2, "志愿者"), (3, "服务公司人员"), (4, '服务中心人员')),
                                      verbose_name=u'服务人员类别')
    booking_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"预约时间")
    begin_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"开始时间")
    return_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"回访时间")
    create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"工单创建时间")

    class Meta:
        verbose_name = u"服务机构待处理"
        verbose_name_plural = verbose_name

class Service_per_pro(models.Model):
    address = models.CharField(max_length=100, verbose_name=u"服务区域")
    work_type = models.IntegerField(default=0, choices=((1, "托底人员"), (2, "自费人员")), verbose_name=u'客户类型')
    name = models.CharField(max_length=50, verbose_name='服务对象')
    mobile = models.CharField(max_length=11, verbose_name=u'老人联系电话')
    mobile_r = models.CharField(max_length=11, verbose_name=u'家属联系电话')
    user_id = models.IntegerField(default=0, verbose_name=u'工单编号')
    satis_type = models.IntegerField(default=0, choices=((1, "满意"), (2, "一般"), (3, "不满意")), verbose_name=u'服务满意度')
    ticket_type = models.IntegerField(default=0, choices=((1, '救助工单'), (2, '投诉工单'), (3, '反馈工单'), (4, '咨询工单'), (5, '急救工单'), (6, '普通工单'), (7, '语音工单')), verbose_name=u'工单类型')
    way = models.IntegerField(default=0, choices=((1, '自费'), (2, '政府补助')), verbose_name=u'收费类型')
    project = models.CharField(max_length=100, verbose_name=u'服务项目')
    address_er = models.CharField(max_length=100, verbose_name=u"服务地址")
    work_name = models.CharField(max_length=50, verbose_name=u'服务机构')
    worker_name = models.CharField(max_length=50, verbose_name='服务人员')
    worker_type = models.IntegerField(default=0, choices=((1, "社工"), (2, "志愿者"), (3, "服务公司人员"), (4, '服务中心人员')),
                                      verbose_name=u'服务人员类别')
    booking_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"预约时间")
    begin_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"开始时间")
    return_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"回访时间")
    create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"工单创建时间")

    class Meta:
        verbose_name = u"服务人员待处理"
        verbose_name_plural = verbose_name

class Service_return(models.Model):
    address = models.CharField(max_length=100, verbose_name=u"服务区域")
    work_type = models.IntegerField(default=0, choices=((1, "托底人员"), (2, "自费人员")), verbose_name=u'客户类型')
    name = models.CharField(max_length=50, verbose_name='服务对象')
    mobile = models.CharField(max_length=11, verbose_name=u'老人联系电话')
    mobile_r = models.CharField(max_length=11, verbose_name=u'家属联系电话')
    user_id = models.IntegerField(default=0, verbose_name=u'工单编号')
    satis_type = models.IntegerField(default=0, choices=((1, "满意"), (2, "一般"), (3, "不满意")), verbose_name=u'服务满意度')
    ticket_type = models.IntegerField(default=0, choices=((1, '救助工单'), (2, '投诉工单'), (3, '反馈工单'), (4, '咨询工单'), (5, '急救工单'), (6, '普通工单'), (7, '语音工单')), verbose_name=u'工单类型')
    way = models.IntegerField(default=0, choices=((1, '自费'), (2, '政府补助')), verbose_name=u'收费类型')
    project = models.CharField(max_length=100, verbose_name=u'服务项目')
    address_er = models.CharField(max_length=100, verbose_name=u"服务地址")
    work_name = models.CharField(max_length=50, verbose_name=u'服务机构')
    worker_name = models.CharField(max_length=50, verbose_name='服务人员')
    worker_type = models.IntegerField(default=0, choices=((1, "社工"), (2, "志愿者"), (3, "服务公司人员"), (4, '服务中心人员')),
                                      verbose_name=u'服务人员类别')
    booking_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"预约时间")
    begin_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"开始时间")
    return_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"回访时间")
    create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"工单创建时间")

    class Meta:
        verbose_name = u"服务机构退单"
        verbose_name_plural = verbose_name

class In_the_service(models.Model):
    address = models.CharField(max_length=100, verbose_name=u"服务区域")
    work_type = models.IntegerField(default=0, choices=((1, "托底人员"), (2, "自费人员")), verbose_name=u'客户类型')
    name = models.CharField(max_length=50, verbose_name='服务对象')
    mobile = models.CharField(max_length=11, verbose_name=u'老人联系电话')
    mobile_r = models.CharField(max_length=11, verbose_name=u'家属联系电话')
    user_id = models.IntegerField(default=0, verbose_name=u'工单编号')
    satis_type = models.IntegerField(default=0, choices=((1, "满意"), (2, "一般"), (3, "不满意")), verbose_name=u'服务满意度')
    ticket_type = models.IntegerField(default=0, choices=((1, '救助工单'), (2, '投诉工单'), (3, '反馈工单'), (4, '咨询工单'), (5, '急救工单'), (6, '普通工单'), (7, '语音工单')), verbose_name=u'工单类型')
    way = models.IntegerField(default=0, choices=((1, '自费'), (2, '政府补助')), verbose_name=u'收费类型')
    project = models.CharField(max_length=100, verbose_name=u'服务项目')
    address_er = models.CharField(max_length=100, verbose_name=u"服务地址")
    work_name = models.CharField(max_length=50, verbose_name=u'服务机构')
    worker_name = models.CharField(max_length=50, verbose_name='服务人员')
    worker_type = models.IntegerField(default=0, choices=((1, "社工"), (2, "志愿者"), (3, "服务公司人员"), (4, '服务中心人员')),
                                      verbose_name=u'服务人员类别')
    booking_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"预约时间")
    begin_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"开始时间")
    return_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"回访时间")
    create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"工单创建时间")

    class Meta:
        verbose_name = u"服务中"
        verbose_name_plural = verbose_name

class To_be_returned(models.Model):
    address = models.CharField(max_length=100, verbose_name=u"服务区域")
    work_type = models.IntegerField(default=0, choices=((1, "托底人员"), (2, "自费人员")), verbose_name=u'客户类型')
    name = models.CharField(max_length=50, verbose_name='服务对象')
    mobile = models.CharField(max_length=11, verbose_name=u'老人联系电话')
    mobile_r = models.CharField(max_length=11, verbose_name=u'家属联系电话')
    user_id = models.IntegerField(default=0, verbose_name=u'工单编号')
    satis_type = models.IntegerField(default=0, choices=((1, "满意"), (2, "一般"), (3, "不满意")), verbose_name=u'服务满意度')
    ticket_type = models.IntegerField(default=0, choices=((1, '救助工单'), (2, '投诉工单'), (3, '反馈工单'), (4, '咨询工单'), (5, '急救工单'), (6, '普通工单'), (7, '语音工单')), verbose_name=u'工单类型')
    way = models.IntegerField(default=0, choices=((1, '自费'), (2, '政府补助')), verbose_name=u'收费类型')
    project = models.CharField(max_length=100, verbose_name=u'服务项目')
    address_er = models.CharField(max_length=100, verbose_name=u"服务地址")
    work_name = models.CharField(max_length=50, verbose_name=u'服务机构')
    worker_name = models.CharField(max_length=50, verbose_name='服务人员')
    worker_type = models.IntegerField(default=0, choices=((1, "社工"), (2, "志愿者"), (3, "服务公司人员"), (4, '服务中心人员')),
                                      verbose_name=u'服务人员类别')
    booking_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"预约时间")
    begin_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"开始时间")
    return_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"回访时间")
    create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"工单创建时间")

    class Meta:
        verbose_name = u"待回访"
        verbose_name_plural = verbose_name

class Closed(models.Model):
    address = models.CharField(max_length=100, verbose_name=u"服务区域")
    work_type = models.IntegerField(default=0, choices=((1, "托底人员"), (2, "自费人员")), verbose_name=u'客户类型')
    name = models.CharField(max_length=50, verbose_name='服务对象')
    mobile = models.CharField(max_length=11, verbose_name=u'老人联系电话')
    mobile_r = models.CharField(max_length=11, verbose_name=u'家属联系电话')
    user_id = models.IntegerField(default=0, verbose_name=u'工单编号')
    satis_type = models.IntegerField(default=0, choices=((1, "满意"), (2, "一般"), (3, "不满意")), verbose_name=u'服务满意度')
    ticket_type = models.IntegerField(default=0, choices=((1, '救助工单'), (2, '投诉工单'), (3, '反馈工单'), (4, '咨询工单'), (5, '急救工单'), (6, '普通工单'), (7, '语音工单')), verbose_name=u'工单类型')
    way = models.IntegerField(default=0, choices=((1, '自费'), (2, '政府补助')), verbose_name=u'收费类型')
    project = models.CharField(max_length=100, verbose_name=u'服务项目')
    address_er = models.CharField(max_length=100, verbose_name=u"服务地址")
    work_name = models.CharField(max_length=50, verbose_name=u'服务机构')
    worker_name = models.CharField(max_length=50, verbose_name='服务人员')
    worker_type = models.IntegerField(default=0, choices=((1, "社工"), (2, "志愿者"), (3, "服务公司人员"), (4, '服务中心人员')),
                                      verbose_name=u'服务人员类别')
    booking_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"预约时间")
    begin_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"开始时间")
    return_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"回访时间")
    create_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"工单创建时间")

    class Meta:
        verbose_name = u"已办结"
        verbose_name_plural = verbose_name
