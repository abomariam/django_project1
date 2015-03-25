from django.conf.urls import patterns, include, url
# from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('user.urls')),
    url(r'^category/', include('cat_forum.cat_urls')),
    url(r'^forum/', include('cat_forum.forum_urls')),
)
