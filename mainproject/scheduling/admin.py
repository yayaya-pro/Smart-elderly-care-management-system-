from django.contrib import admin
import xadmin
# Register your models here.
from .models import Work_order, Service_per_pro, Service_processed, Service_return, In_the_service, Closed, To_be_returned

class Work_orderAdmin(object):
    list_display = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'ticket_status', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type', 'booking_time', 'begin_time', 'return_time', 'create_time']
    search_fields = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'ticket_status', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type']
    list_filter = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'ticket_status', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type', 'booking_time', 'begin_time', 'return_time', 'create_time']

class Service_per_proAdmin(object):
    list_display = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type',  'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type', 'booking_time', 'begin_time', 'return_time', 'create_time']
    search_fields = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type',  'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type']
    list_filter = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type',  'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type', 'booking_time', 'begin_time', 'return_time', 'create_time']

class Service_processedAdmin(object):
    list_display = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type', 'booking_time', 'begin_time', 'return_time', 'create_time']
    search_fields = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type']
    list_filter = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type', 'booking_time', 'begin_time', 'return_time', 'create_time']

class Service_returnAdmin(object):
    list_display = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type', 'booking_time', 'begin_time', 'return_time', 'create_time']
    search_fields = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type']
    list_filter = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type', 'booking_time', 'begin_time', 'return_time', 'create_time']

class In_the_serviceAdmin(object):
    list_display = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type', 'booking_time', 'begin_time', 'return_time', 'create_time']
    search_fields = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type']
    list_filter = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type', 'booking_time', 'begin_time', 'return_time', 'create_time']

class ClosedAdmin(object):
    list_display = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type', 'booking_time', 'begin_time', 'return_time', 'create_time']
    search_fields = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type']
    list_filter = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type', 'booking_time', 'begin_time', 'return_time', 'create_time']

class To_be_returnedAdmin(object):
    list_display = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type','way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type', 'booking_time', 'begin_time', 'return_time', 'create_time']
    search_fields = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type']
    list_filter = ['address', 'work_type', 'name', 'mobile', 'mobile_r', 'user_id', 'satis_type', 'ticket_type', 'way', 'project', 'address_er', 'work_name', 'worker_name', 'worker_type', 'booking_time', 'begin_time', 'return_time', 'create_time']

xadmin.site.register(Work_order, Work_orderAdmin)
xadmin.site.register(Service_processed, Service_processedAdmin)
xadmin.site.register(Service_per_pro, Service_per_proAdmin)
xadmin.site.register(Service_return, Service_returnAdmin)
xadmin.site.register(In_the_service, In_the_serviceAdmin)
xadmin.site.register(To_be_returned, To_be_returnedAdmin)
xadmin.site.register(Closed, ClosedAdmin)