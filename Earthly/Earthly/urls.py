from django.conf.urls import patterns, include, url
from django.contrib import admin
from TwitterQuery import twitterhandler, views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Earthly.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.globe_page_view),
<<<<<<< HEAD
    url(r'^test/$', twitterhandler.get_tweets),
=======

    #url(r'^testtwit/$', twitterhandler.get_tweets),

    #what do we do here?
    #url(r'^background/([0-9]{4})/([0-9]{2})/' views.month_archive),
    
    #requires: none
    #returns: json [{username:score},...]
    url(r'^leaderboard/', views.leaderboard),
    #requires: ?users=name,name,...
    url(r'^scoreuser/', views.userscores),

    url(r'^test/$', views.test_view),

>>>>>>> FETCH_HEAD
)
