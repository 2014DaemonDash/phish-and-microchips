from django.shortcuts import render

def globe_page_view(request):
    return render(request,'globeTest.html',None)
