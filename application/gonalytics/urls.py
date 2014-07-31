from django.conf.urls import patterns, include, url
from django.contrib import admin

from dashboard.views import Dashboard

urlpatterns = patterns('',
    url(r'^$', include('dashboard.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^visit/', include('visit.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
