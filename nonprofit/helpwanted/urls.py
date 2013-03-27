from django.conf.urls import *
from nonprofit.helpwanted.feeds import OpenPositionsFeed
from nonprofit.helpwanted.views import JobDetail, JobList

urlpatterns = patterns(
    '',
    url(r'^rss/$', OpenPositionsFeed(), name="job_feed"),
    url(r'^(?P<pk>\d+)/', JobDetail.as_view(), name="job_detail"),
    url(r'^$', JobList.as_view(), name="job_list"),
)
