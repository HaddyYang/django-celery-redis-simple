#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog
from .tasks import sendmail
import json

def home(request):
    #耗时任务，发送邮件
    sendmail.delay('test@test.com')

    #其他行为
    data = list(Blog.objects.values('caption'))
    return HttpResponse(json.dumps(data), content_type = 'application/json')
