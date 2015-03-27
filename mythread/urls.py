from django.conf.urls import patterns, include, url
from mythread.views import *

urlpatterns = patterns('',
    url(r'^$', listThread),
    url(r'add/(?P<forum_id>\d+)$',addThread),
    url(r'edit/(?P<id>\d+)$',editThread),
    url(r'list/(?P<id>\d+)$',list_replies),
    url(r'delete/(?P<id>\d+)$',delThread)
)
