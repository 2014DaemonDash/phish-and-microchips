from django.shortcuts import render
from django.http import HttpResponse
import json

def globe_page_view(request):
    return render(request,'globeTest.html',None)


def leaderboard(request):
    
    #enter the leaders here
    leaders = {'firstleader':2134213,'secondleader':2134212,}
    
    return HttpResponse(json.dumps(leaders))

def userscores(request):
    return HttpResponse("unimplemented")

def test_view(request):
    return HttpResponse("hello world");



