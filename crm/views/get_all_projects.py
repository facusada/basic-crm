from django.http import JsonResponse
from django.views import View
from ..models import Project


class GetAllProjects(View):
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all().values('id', 'name', 'description', 'created_at')
        projects_list = list(projects)
        return JsonResponse(projects_list, safe=False)