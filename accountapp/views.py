from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    # return HttpResponse('Hello world!')
    # return render(request, 'base.html')

    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html', context={'text':'POST METHOD'})
    else :
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD'})

    # return render(request, 'accountapp/hello_world.html')
