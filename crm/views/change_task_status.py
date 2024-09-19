from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Task
from ..services.change_status_service import ChangeStatusTaskService

class ChangeTaskStatusView(APIView):
    def post(self, request, project_id, task_id):
        try:
            ChangeStatusTaskService.change_status(project_id, request.data, task_id)

            return Response({'message': 'Task status updated successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # task = get_object_or_404(Task, id=task_id, project_id=project_id)
        
        # new_status = request.data.get('status')

        # if new_status in ['pending', 'in_progress', 'completed']:
        #     task.status = new_status
        #     task.save()
        #     return Response({'message': 'Task status updated successfully'}, status=status.HTTP_200_OK)
        
        # return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)