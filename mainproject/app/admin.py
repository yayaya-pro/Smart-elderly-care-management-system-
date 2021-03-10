from django.contrib import admin

# Register your models here.
import xadmin

# Register your models here.
from .models import EmailVerifyRecord, User

from xadmin import views

class GlobalSetting(object):
    # 设置后台顶部标题
    site_title ='云晖后台管理系统'
# 设置后台底部标题
    site_footer ='云晖-无感陪护自助居家养老院'



#设置菜单可折叠

xadmin.site.register(views.CommAdminView, GlobalSetting)

class UserAdmin(object):
    model_icon = 'fa  fa-home'

class BaseSetting(object):
    # 启用主题管理器
    enable_themes = True
    # 使用主题
    #use_bootswatch = True
    user_themes = [
        {'name': 'Cerulean', 'css': 'https://bootswatch.com/3/cerulean/bootstrap.css'},
        {'name': 'Cosmo', 'css': 'https://bootswatch.com/3/cosmo/bootstrap.css'},
        {'name': 'Cyborg', 'css': 'https://bootswatch.com/3/cyborg/bootstrap.css'},
        {'name': 'Darkly', 'css': 'https://bootswatch.com/3/darkly/bootstrap.css'},
        {'name': 'Flatly', 'css': 'https://bootswatch.com/3/flatly/bootstrap.css'}

    ]



class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']




xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

# 注册主题设置

xadmin.site.register(views.BaseAdminView, BaseSetting)


#注册学生表到后台管理

xadmin.site.register(User, UserAdmin)
