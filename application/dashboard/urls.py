from django.conf.urls import patterns, url
from dashboard.views import Dashboard

urlpatterns = patterns(
    '',
    url(r'^$', Dashboard.as_view(), name='dashboard'),
)
