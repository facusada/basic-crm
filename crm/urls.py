from django.urls import path

from crm.views.change_task_status import ChangeTaskStatusView
from crm.views.create_task import TaskCreateView
from crm.views.get_tasks import TaskListView
from crm.views.project_detail import ProjectDetailView
from .views.get_all_projects import GetAllProjects
from .views.create_project import ProjectCreateView

urlpatterns = [
    path('get-projects/', GetAllProjects.as_view(), name='get_projects'),
    path('new-projects/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:project_id>/tasks/', TaskListView.as_view(), name='task_list'),
    path('project/<int:project_id>/task/add/', TaskCreateView.as_view(), name='task_create'),
    path('project/<int:project_id>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:project_id>/task/<int:task_id>/change-status/', ChangeTaskStatusView.as_view(), name='change_task_status'),
]