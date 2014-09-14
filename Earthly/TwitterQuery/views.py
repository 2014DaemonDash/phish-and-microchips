from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
import json
=======
>>>>>>> e93cf83c73bb1c7c337351dffbf52087db8b4c64

def globe_page_view(request):
    return render(request,'globeTest.html',None)

<<<<<<< HEAD

def leaderboard(request):
    
    #enter the leaders here
    leaders = {'firstleader':2134213,'secondleader':2134212,}
    
    return HttpResponse(json.dumps(leaders))

def userscores(request):
    return HttpResponse("unimplemented")
=======
def test_view(request):
    return HttpResponse("hello world");


>>>>>>> e93cf83c73bb1c7c337351dffbf52087db8b4c64
