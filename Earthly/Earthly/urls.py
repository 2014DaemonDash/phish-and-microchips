from django.conf.urls import patterns, include, url
from django.contrib import admin
from TwitterQuery import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Earthly.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.globe_page_view),
    url(r'^test/$', views.test_view),
)
