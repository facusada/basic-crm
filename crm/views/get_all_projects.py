from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services.get_all_projects_service import ProjectService
from ..serializers.projects_serializer import ProjectSerializer

class GetAllProjectsView(APIView):
    def get(self, request):
        try:
            projects = ProjectService.get_all_projects()
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)