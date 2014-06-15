from django.conf.urls import patterns, url
from user.views import Login, Logout

urlpatterns = patterns(
    '',
    url(r'^login/$', Login.as_view(), name='user_login'),
    url(r'^logout/$', Logout.as_view(), name='user_logout'),
)
