from django.conf.urls import patterns, include, url

from django.contrib import admin
from blog import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbs.views.home', name='home'),
    url(r'^$', views.index),

    url(r'^detail/(\d+)/$', views.bbs_detail),
    url(r'^detail/\d+/sub_comment/$', views.sub_comment),
    url(r'^bbs_pub/$', views.bbs_pub),
    url(r'^bbs_sub/$', views.bbs_sub),
    url(r'^category/(\d+)/$', views.category),
	
)
