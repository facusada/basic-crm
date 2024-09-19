from django.shortcuts import get_object_or_404
from ..models import Task

class ChangeStatusTaskService:
    @staticmethod
    def change_status(project_id, task_data, task_id):
        task = get_object_or_404(Task, id=task_id, project_id=project_id)
        
        new_status = task_data.get('status')

        if new_status in ['pending', 'in_progress', 'completed']:
            task.status = new_status
            task.save()

        return task