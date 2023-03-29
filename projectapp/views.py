from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView

from projectapp import models
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project


# Create your views here.

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def form_valid(self, form):
        temp_project = form.save(commit=False)
        temp_project.writer = self.request.user
        temp_project.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView):
    model = Project
    form_class = ProjectCreationForm
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'


class ProjectListView(ListView):
    models = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25  # 한페이지 당 글 개수

    def get_queryset(self):
        return models.Project.objects.order_by('created_at')
