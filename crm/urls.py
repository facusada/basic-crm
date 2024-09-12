from django.urls import path
from .views.get_all_projects import GetAllProjects
from .views.create_project import ProjectCreateView

urlpatterns = [
    path('get-projects/', GetAllProjects.as_view(), name='get_projects'),
    path('new-projects/', ProjectCreateView.as_view(), name='project_create'),
]