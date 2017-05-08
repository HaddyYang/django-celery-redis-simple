#coding:utf-8
from celery.decorators import task 
import time

#异步任务
@task
def sendmail(email):
    print('start send email to %s' % email)
    time.sleep(5) #休息5秒
    print('success')
    return True


#定时任务
from celery.task.schedules import crontab  
from celery.decorators import periodic_task  

#每分钟执行一次
#http://docs.celeryproject.org/en/master/userguide/periodic-tasks.html
@periodic_task(run_every=crontab())
def some_task():
    print('periodic task test!!!!!')
    time.sleep(5)
    print('success')
    return True