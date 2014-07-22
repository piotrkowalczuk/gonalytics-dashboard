from django.conf.urls import patterns, url
from visit.views import VisitList

urlpatterns = patterns(
    '',
    url(r'^$', VisitList.as_view(), name='visit_list'),
)
