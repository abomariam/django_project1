from django.conf.urls import patterns, include, url
from cat_forum.views import *

urlpatterns = patterns('',
    url(r'^add/$', forum_add),
    url(r'^list/$', forum_list),
    url(r'^edit/(?P<id>\d+)', forum_edit),
    url(r'^delete/(?P<id>\d+)$', forum_delete),
)