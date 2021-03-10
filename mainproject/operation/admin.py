from django.contrib import admin

# Register your models here.
import xadmin
from .models import UserComments, Cost, Service, Service_person, CityDict
from operation import models
from xadmin import views

class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CostAdmin(object):
    list_display = ['way', 'change_price', 'add_time']
    search_fields = ['way', 'change_price']
    list_filter = ['way', 'change_price', 'add_time']

class ServiceAdmin(object):
    list_display = ['city', 'work_type', 'work_name', 'desc', 'address', 'mobile', 'fav_nums', 'image', 'audit_status', 'add_time']
    search_fields = ['city', 'work_type', 'work_name', 'desc', 'address', 'mobile', 'fav_nums', 'image', 'audit_status']
    list_filter = ['city', 'work_type', 'work_name', 'desc', 'address', 'mobile', 'fav_nums', 'image', 'audit_status', 'add_time']

class Service_personAdmin(object):
    list_display = ['org', 'worker_name', 'mobile', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'creator', 'add_time']
    search_fields = ['org', 'worker_name', 'mobile', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'creator']
    list_filter = ['org', 'worker_name', 'mobile', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'creator', 'add_time']

class UserCommentsAdmin(object):
    list_display = ['user', 'work_name', 'worker_name', 'name', 'comments', 'add_time']
    search_fields = ['user', 'work_name', 'worker_name', 'name', 'comments']
    list_filter = ['user', 'work_name', 'worker_name', 'name', 'comments', 'add_time']



xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(Cost, CostAdmin)
xadmin.site.register(Service, ServiceAdmin)
xadmin.site.register(Service_person, Service_personAdmin)
xadmin.site.register(UserComments, UserCommentsAdmin)