# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import Http404
from .tasks import tester_task_1, tester_task_2

def test_celery_beat(request):
    '''
    测试关闭celery beat view主动触发是否可以处理任务

        curl localhost:9000/test_celery_app
        或者浏览器输入

        并在flower中 localhost:5555查看任务情况

    '''
    tester_task_1.delay()
    raise Http404
