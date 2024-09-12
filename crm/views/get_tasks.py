from django.shortcuts import render, get_object_or_404
from django.views import View
from ..models import Project, Task

class TaskListView(View):
    def get(self, request, project_id):
        project = get_object_or_404(Project, id=project_id)
        tasks = Task.objects.filter(project=project)
        return render(request, 'crm/task_list.html', {'project': project, 'tasks': tasks})