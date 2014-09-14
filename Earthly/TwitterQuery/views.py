from django.shortcuts import render
from django.http import HttpResponse

def globe_page_view(request):
    return render(request,'globeTest.html',None)

def test_view(request):
    return HttpResponse("hello world");


