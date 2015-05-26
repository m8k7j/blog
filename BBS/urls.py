from django.conf.urls import patterns, include, url

from django.contrib import admin
from blog import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbs.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$',views.login),
	url(r'^acc_login/$',views.acc_login),
	url(r'^logout/$',views.logout_view),
	url(r'accounts/login/$','django.contrib.auth.views.login'),
	url(r'^$', views.index),
)
