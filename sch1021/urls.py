from django.conf.urls import patterns, include, url
from journal import urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sch1021.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('journal.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
