#coding:utf-8
from __future__ import absolute_import
from celery.decorators import task 
import time

#异步任务
@task
def sendmail(email):
    print('start send email to %s' % email)
    time.sleep(5) #休息5秒
    print('success')
    return True

#bind等于True则绑定到celery app对象，可使用app的方法
@task(bind=True)
def err_retry(self, email):
    try:
        a = 1/0
    except Exception as e:
        #尝试重新执行1次任务
        raise self.retry(exc=e)


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