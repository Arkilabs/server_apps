from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'serverapp.views.home', name='home'),
    url(r'^start/$', 'serverapp.views.start', name='start'),
    url(r'^stop/$', 'serverapp.views.stop', name='stop'),
)
