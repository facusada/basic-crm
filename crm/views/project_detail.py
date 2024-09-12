from django.shortcuts import render, get_object_or_404
from django.views import View#+
from ..models import Project

class ProjectDetailView(View):
    def get(self, request, project_id):
        project = get_object_or_404(Project, id=project_id)
        return render(request, 'crm/project_detail.html', {'project': project})
