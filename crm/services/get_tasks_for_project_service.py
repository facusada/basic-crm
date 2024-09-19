from ..models import Project, Task

class TaskService:
    @staticmethod
    def get_tasks_for_project(project_id):
        project = Project.objects.get(id=project_id)
        tasks = Task.objects.filter(project=project)
        return tasks