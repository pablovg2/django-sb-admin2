from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_sb_admin_v2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'sb_admin2.views.home')
)
