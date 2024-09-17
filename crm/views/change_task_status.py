from django.shortcuts import get_object_or_404, redirect
from django.views import View
from ..models import Task

class ChangeTaskStatusView(View):
    def post(self, request, project_id, task_id):
        task = get_object_or_404(Task, id=task_id, project_id=project_id)
        
        new_status = request.POST.get('status')

        if new_status in ['pending', 'in_progress', 'completed']:
            task.status = new_status
            task.save()
        
        return redirect('task_list', project_id=project_id)