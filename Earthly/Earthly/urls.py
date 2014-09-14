from django.conf.urls import patterns, include, url
from django.contrib import admin
from TwitterQuery import twitterhandler, views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Earthly.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.globe_page_view),
    url(r'^test/$', twitterhandler.get_tweets),
    
    #requires: none
    #returns json object {'name':score,...}
    url(r'^leaderboard/', views.leaderboard),
    #requires: ?users='name1,name3,...'
    #returns: json object {'name1':score,'name3':score,...}
    url(r'^scoreuser/', views.userscores),
    url(r'^tweetpipeline/', views.tweetpipeline),
)
