from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Project

class ProjectCreateView(APIView):
    def post(self, request):
        data = request.data
        try:
            project = Project.objects.create(
                name=data.get('name'),
                description=data.get('description')
            )
            response_data = {
                'id': project.id,
                'name': project.name,
                'description': project.description,
                'created_at': project.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)