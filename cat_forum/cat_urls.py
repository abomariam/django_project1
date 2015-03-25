from django.conf.urls import patterns, include, url
from cat_forum.views import *

urlpatterns = patterns('',
    url(r'^list$', cat_list),
    url(r'^add/$', cat_add),
    url(r'^edit/(?P<id>\d+)', cat_edit),
    url(r'^delete/(?P<id>\d+)$', cat_delete),
)