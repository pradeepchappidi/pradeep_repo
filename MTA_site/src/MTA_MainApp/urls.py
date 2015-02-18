from django.conf.urls import patterns, include, url
from django.contrib import admin
from MTA_MainApp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MTA_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^$', views.introduction, name = 'introduction'),
)
