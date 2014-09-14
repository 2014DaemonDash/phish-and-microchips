from django.shortcuts import render
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
    leaders = {'firstleader':2134213,'secondleader':2134212,}
    
    return HttpResponse(json.dumps(leaders))

def userscores(request):
    out = {}

    users = request.GET.get('users',"").split(',')
    #set this with the user data
    db = {'alice':123,'bob':456,'charlie':789}
    
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
    
    if lat_max is None or lat_min is None or lon_min is None or lon_max is None:
        return HttpResponse("")
    
    tweets = dbhandler.query_db(lat_min, lat_max, lon_min, lon_max, dt)
    
    dicts = [obj.as_dict() for obj in tweets]
    
    print tweets,dt
    
    return HttpResponse(json.dumps(dicts))



