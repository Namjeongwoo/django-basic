from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image']