from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'idlhands_app.views.home', name='home'),
    # url(r'^idlhands/', include('idlhands.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<username>\w+)/$', 'idlhands_app.views.user_profile', name="profile"),
    url(r'^(?P<username>\w+)/(?P<id>\d+)/$', 'idlhands_app.views.project'),
    url(r'^login', 'idlhands_app.views.login_page', name='login'),
    url(r'^new', 'idlhands_app.views.new_user', name='new'),
    url(r'^logout', 'idlhands_app.views.logout_page', name='logout'),
    url(r'^users', 'idlhands_app.views.users', name='users'),
    url(r'^projects', 'idlhands_app.views.projects', name='projects'),
)
