from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView
from projectapp.views import ProjectCreateView, ProjectDetailView, ProjectListView, ProjectUpdateView, ProjectDeleteView

app_name = "projectapp"

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
    #path('update/<int:pk>', ProjectUpdateView.as_view(template_name='projectapp/update.html'), name='update'),
    path('update/<int:pk>', ProjectUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ProjectDeleteView.as_view(template_name='projectapp/delete.html'), name='delete'),
    path('list/', ProjectListView.as_view(), name='list'),

]