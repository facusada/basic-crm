from ..models import Task

class GetAllProjectsTransformer:
    @staticmethod
    def transform_projects_to_boards():
        todo_tasks = Task.objects.filter(status='pending').values('id', 'title', 'description')
        inprogress_tasks = Task.objects.filter(status='in_progress').values('id', 'title', 'description')
        done_tasks = Task.objects.filter(status='completed').values('id', 'title', 'description')

        boards = [
            {
                'id': 'todo',
                'title': 'Por hacer',
                'tasks': list(todo_tasks)
            },
            {
                'id': 'inprogress',
                'title': 'En progreso',
                'tasks': list(inprogress_tasks)
            },
            {
                'id': 'done',
                'title': 'Hecho',
                'tasks': list(done_tasks)
            }
        ]

        return boards