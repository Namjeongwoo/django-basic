from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):
    # return HttpResponse('Hello world!')
    # return render(request, 'base.html')

    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld() # 객체 생성
        new_hello_world.text = temp # input data hello_world.text 저장
        new_hello_world.save()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_output':new_hello_world})
    else :
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD'})

    # return render(request, 'accountapp/hello_world.html')
