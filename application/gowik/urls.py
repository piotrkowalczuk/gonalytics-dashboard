from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^user/', include('user.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
