from django.conf.urls import patterns, include, url
from user.views import *

urlpatterns = patterns('',
    url(r'add$', add_user),
    url(r'profile/(?P<id>\d+)$', profile_user),
    url(r'register$', register_user),
    url(r'login$', login_user),
    url(r'logout$', logout_user),
    url(r'^$', list_users),
    url(r'edit/(?P<id>\d+)$', edit_user),
    url(r'delete/(?P<id>\d+)$', delete_user),
)