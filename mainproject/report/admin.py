from django.contrib import admin
import xadmin
# Register your models here.
from .models import ReportManage, WorkOrderDetail

class ReportManageAdmin(object):
    list_display = ['title', 'url', 'start']
    search_fields = ['title', 'url', 'start']
    list_filter = ['title', 'url', 'start']

class WorkOrderDetailAdmin(object):
    list_display = ['address', 'name', 'deductions', 'user_id', 'ticket_status', 'work_name', 'worker_name', 'create_time', 'return_time']
    search_fields = ['address', 'name', 'deductions', 'user_id', 'ticket_status', 'work_name', 'worker_name']
    list_filter = ['address', 'name', 'deductions', 'user_id', 'ticket_status', 'work_name', 'worker_name', 'create_time', 'return_time']

xadmin.site.register(ReportManage, ReportManageAdmin)
xadmin.site.register(WorkOrderDetail, WorkOrderDetailAdmin)