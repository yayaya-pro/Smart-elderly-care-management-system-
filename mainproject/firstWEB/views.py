from __future__ import unicode_literals
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from firstWEB import models

# Create your views here.

def index(request):
    return render(request, 'index.html')

def calpage(request):
    return render(request, 'cal.html')

def cal(request):
    if request.POST:
        value_a = request.POST['valueA']
        value_b = request.POST['valueB']
        result = int(value_a) + int(value_b)
        models.cal.objects.create(value_a=value_a, value_b=value_b, result=result)
    else:
        return HttpResponse('please visit us with POST')
    return render(request, 'result.html', context={'data': result})

def callist(request):
    data = models.cal.objects.all()
    #for i in data:
    #   print(i.value_a, i.value_b, i.result)
    return render(request, 'list.html', context={'data': data})

def deldata(request):
    models.cal.objects.all().delete()
    return HttpResponse('Data Deleted')


