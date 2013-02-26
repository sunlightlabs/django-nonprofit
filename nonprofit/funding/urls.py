from django.conf.urls import *

urlpatterns = patterns('nonprofit.funding.views',
    url(r'^funding/$', 'funding', name='funding'),
    url(r'^funding.(?P<ext>[a-z]{3})$', 'funding_download', name='funding_download'),
    url(r'^grants/$', 'grants', name='grants'),
)
