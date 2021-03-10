from django.contrib import admin
import xadmin
from .models import ZifeiUsers, TuodiUsers, ServeOrg, ServerOrg
# Register your models here.
# 设计左侧菜单

class ZifeiUsersAdmin(object):
    list_display = ['name_z', 'mobile_r', 'address', 'id_number', 'user_birth', 'mobile', 'user_id', 'work_type', 'worker_name', 'send_time']
    search_fields = ['name_z', 'address', 'mobile_r', 'id_number', 'mobile', 'user_birth', 'user_id', 'work_type', 'worker_name']
    list_filter = ['name_z', 'address', 'id_number', 'mobile_r', 'mobile', 'user_birth', 'user_id', 'work_type', 'worker_name', 'send_time']

class TuodiUsersAdmin(object):
    list_display = ['name', 'address', 'mobile_r', 'id_number', 'user_birth', 'mobile', 'user_id', 'work_type', 'worker_name', 'send_time']
    search_fields = ['name', 'address', 'mobile_r', 'id_number', 'mobile', 'user_birth', 'user_id', 'work_type', 'worker_name']
    list_filter = ['name', 'address', 'mobile_r', 'id_number', 'mobile', 'user_birth', 'user_id', 'work_type', 'worker_name', 'send_time']

class ServeOrgAdmin(object):
    list_display = ['address', 'work_name', 'work_type', 'name', 'mobile', 'user_id', 'satis_type', 'work_type', 'add_time', 'worker_name', 'worker_type']
    search_fields = ['address', 'work_name', 'work_type', 'name', 'mobile', 'user_id', 'satis_type', 'work_type',  'worker_name', 'worker_type']
    list_filter = ['address', 'work_name', 'work_type', 'name', 'mobile', 'user_id', 'satis_type', 'work_type', 'add_time', 'worker_name', 'worker_type']

class ServerOrgAdmin(object):
    list_display = ['address_s', 'work_name', 'work_type', 'name', 'mobile', 'user_id', 'satis_type', 'work_type', 'add_time', 'worker_name', 'worker_type']
    search_fields = ['address_s', 'work_name', 'work_type', 'name', 'mobile', 'user_id', 'satis_type', 'work_type',  'worker_name', 'worker_type']
    list_filter = ['address_s', 'work_name', 'work_type', 'name', 'mobile', 'user_id', 'satis_type', 'work_type', 'add_time', 'worker_name', 'worker_type']

xadmin.site.register(TuodiUsers, TuodiUsersAdmin)
xadmin.site.register(ZifeiUsers, ZifeiUsersAdmin)
xadmin.site.register(ServeOrg, ServeOrgAdmin)
xadmin.site.register(ServerOrg, ServerOrgAdmin)