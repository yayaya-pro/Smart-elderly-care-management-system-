from django.contrib import admin

# Register your models here.
import xadmin
from .models import Test

from xadmin import views

class TestAdmin(object):
	list_display = []
	object_list_template = "test.html"

xadmin.site.register(Test, TestAdmin)