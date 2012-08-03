from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'idlhands_app.views.home', name='home'),
    # url(r'^idlhands/', include('idlhands.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<username>\w+)/$', 'idlhands_app.views.user'),
    url(r'^(?P<username>\w+)/(?P<id>\d+)/$', 'idlhands_app.views.project'),
)
