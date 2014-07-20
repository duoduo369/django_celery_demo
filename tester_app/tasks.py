# -*- coding: utf-8 -*-
from celery.task import task
from django.conf import settings

@task(bind=True, queue=settings.HIGH_PRIORITY_QUEUE)
def tester_task_1(self):
    print self
    print 'only a simply function'

@task()
def tester_task_2():
    print 'also a simply function'
