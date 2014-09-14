from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from TwitterQuery import models
import json
import datetime
import dbhandler

def globe_page_view(request):
    return render(request,'globeTest.html',None)
def cesHW(request):
    return render(request,'HelloWorld.html',None)

def leaderboard(request):
    
    #enter the leaders here
    leaders = [
               {'name':'johnny tablecloth','score':2242},
               {'name':'techabunch','score':2113},
               {'name':'georgepancakes','score':1263},
               {'name':'kernie12','score':1223},
               {'name':'bobwagnerwhynot?','score':849},
               {'name':'capt_awsm_123','score':272},
               ]
    
    return render_to_response('leader.html',{'leaders':leaders})

def about(request):
    return render(request,'about.html',None)

def userscores(request):
    out = {}
    db = {}
    
    # requested users
    users = request.GET.get('users',"").split(',')
    
    #all users
    all = models.TwitterUser.objects.all();
    for rec in all:   
        db[rec.name] = rec.score
    
    for k,v in db.iteritems():
        if k in users:
            out[k]=v
        
    return HttpResponse(json.dumps(out))

def test_view(request):
    return HttpResponse("hello world");

def tweetpipeline(request):
    old_time = request.GET.get('old_time',0)
    lat_max = request.GET.get('max_latitude',None)
    lon_max = request.GET.get('max_longitude',None)
    lat_min = request.GET.get('min_latitude',None)
    lon_min = request.GET.get('min_longitude',None)
    
    dt = datetime.timedelta(milliseconds=int(old_time)) + datetime.datetime(year=1970,month=1,day=1)
    
#     print "dt:"+str(dt)
    
    if lat_max is None or lat_min is None or lon_min is None or lon_max is None:
        return HttpResponse("")
    
    tweets = dbhandler.query_db(lat_min, lat_max, lon_min, lon_max, dt)
    
#     print "tweet:"+repr(tweets[0].datetime)
    
    dicts = [obj.as_dict() for obj in tweets]
    
    return HttpResponse(json.dumps(dicts))



