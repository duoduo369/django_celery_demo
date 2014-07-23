from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^test_celery_app$', 'tester_app.views.test_celery_beat'),
)
