from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services.create_task_service import TaskService


class TaskCreateView(APIView):
    def post(self, request, project_id):
        task_data = request.data

        try:
            task = TaskService.create_task(project_id, task_data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        response_data = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'due_date': task.due_date,
            'project': task.project.id,
            'created_at': task.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': task.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        }
        return Response(response_data, status=status.HTTP_201_CREATED)