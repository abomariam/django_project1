from django.conf.urls import patterns, include, url
from user_messages.views import *


urlpatterns = patterns('',
    # url(r'^(?P<sender_id>\d+)$', messages_list),
    url(r'^(?P<id>\d+)$', messages_get),
    url(r'^$', messages_index),
    # url(r'^add/(?P<sender_id>\d+)$', messages_add),

)
