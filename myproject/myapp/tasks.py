#coding:utf-8
from celery.decorators import task 
import time

@task
def sendmail(email):
    print('start send email to %s' % email)
    time.sleep(5) #休息5秒
    print('success')
    return True
