from django.conf.urls import patterns, include, url
# from django.contrib import admin
from .views import *

urlpatterns = patterns('',

    url(r'^$', index_action),

    url(r'^user/', include('user.urls')),
    url(r'^replay/', include('replay.urls')),
    url(r'^category/', include('cat_forum.cat_urls')),
    url(r'^forum/', include('cat_forum.forum_urls')),
    url(r'^thread/', include('thread.urls')),
)
