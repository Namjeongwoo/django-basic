from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'), # 함수형 View

    # Class View
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
    # datail 접근하기 위한 primary key 포함
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),

]