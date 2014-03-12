
from django.conf.urls import patterns, url
from journal import views

urlpatterns = patterns('',
    url(r'^tasks/$', views.TaskList.as_view(), name='list'),
    url(r'^$', views.main, name='list'),
    url(r'^logout/$', views.logout, name='logout'),
)
