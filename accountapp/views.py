from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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

        hello_world_list = HelloWorld.objects.all() # 객체에 모든 것을 담는다.


        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()  # 객체에 모든 것을 담는다.
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        # return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD'})

