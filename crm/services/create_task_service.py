from django.core.exceptions import ObjectDoesNotExist
from ..models import Task, Project

class TaskService:
    @staticmethod
    def create_task(project_id, task_data):
        try:
            project = Project.objects.get(id=project_id)
        except ObjectDoesNotExist:
            raise ValueError(f"Project with id {project_id} does not exist")
        
        task = Task(
            title=task_data.get('title'),
            description=task_data.get('description'),
            status=task_data.get('status', 'pending'),
            due_date=task_data.get('due_date'),
            project=project
        )
        task.save()

        return task