from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')
        # 객체 생성
        new_hello_world = HelloWorld()
        # input data hello_world.text 저장
        new_hello_world.text = temp
        # model 저장
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()  # 객체에 모든 것을 담는다.

        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()  # 객체에 모든 것을 담는다.
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        # return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD'})


class AccountCreateView(CreateView):
    model = User  # 장고 제공 User Class
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    # Class Based View : reverse_lazy()
    # Function Based View : reverse()
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):
    model = User  # 장고 제공 User Class
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User  # 장고 제공 User Class
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
