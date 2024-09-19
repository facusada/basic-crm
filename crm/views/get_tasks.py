from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services.get_tasks_for_project_service import TaskService
from ..serializers.get_tasks_for_project_serializer import TaskSerializer

class GetTasksForProjectView(APIView):
    def get(self, request, project_id):
        try:
            tasks = TaskService.get_tasks_for_project(project_id)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            