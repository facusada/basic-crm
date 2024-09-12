from django.views.generic import ListView
from ..models import Project


class GetAllProjects(ListView):
    model = Project
    template_name = 'crm/project_list.html'