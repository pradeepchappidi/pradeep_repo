from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MTA_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^MTA/', include('MTA_MainApp.urls')),
)
