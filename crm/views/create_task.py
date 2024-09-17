from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from ..models import Project
from ..forms import TaskForm

class TaskCreateView(View):
    def get(self, request, project_id):
        project = get_object_or_404(Project, id=project_id)
        form = TaskForm(initial={'project': project})
        return render(request, 'crm/create_task.html', {'form': form, 'project': project})

    def post(self, request, project_id):
        project = get_object_or_404(Project, id=project_id)
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('get_projects')
        return render(request, 'crm/create_task.html', {'form': form, 'project': project})