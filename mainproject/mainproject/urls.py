"""mainproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from firstWEB import views

import xadmin
from django.conf.urls import url
from django.views.generic import TemplateView



urlpatterns = [
    url(r'^xadmin', xadmin.site.urls),
    url(r'^index',views.index),
    url(r'^calpage', views.calpage),
    url(r'^cal', views.cal),
    url(r'^list', views.callist),
    url(r'^del', views.deldata),
    url('^$', TemplateView.as_view(template_name='主页面.html'), name='主页面'),
    url('^免责声明/$', TemplateView.as_view(template_name='免责声明.html'), name='免责声明'),
    url('^关于我们/$', TemplateView.as_view(template_name='关于我们.html'), name='关于我们'),
    url('^登录/$', TemplateView.as_view(template_name='登录.html'), name='登录'),
    url('^表单信息/$', TemplateView.as_view(template_name='表单信息.html'), name='表单信息'),
    url('^预约下单/$', TemplateView.as_view(template_name='预约下单.html'), name='预约下单'),
    url('^主页面/$', TemplateView.as_view(template_name='主页面.html'), name='主页面'),
    

]
