
from django.conf.urls import patterns, url
from journal import views

urlpatterns = patterns('',
    url(r'^tasks/$', views.TaskList.as_view(), name='list'),
    url(r'^$', views.main, name='list'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^login/$', views.login, name = "login"),
    url(r'^add_task/$', views.add_task, name='add_task'),

)
