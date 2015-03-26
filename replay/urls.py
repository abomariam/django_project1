from django.conf.urls import patterns, include, url
from replay.views import *

urlpatterns = patterns('',
    url(r'^$', listReplay),
    url(r'add$', addReplay),
    url(r'edit/(?P<id>\d+)$', editReplay),
    url(r'delete/(?P<id>\d+)$', delReplay)
)
