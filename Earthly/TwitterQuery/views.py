from django.shortcuts import render
from django.http import HttpResponse
import json

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



