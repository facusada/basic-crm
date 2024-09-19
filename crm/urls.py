from django.urls import path

from crm.views.change_task_status import ChangeTaskStatusView
from crm.views.create_task import TaskCreateView
from crm.views.get_tasks import GetTasksForProjectView
from .views.get_all_projects import GetAllProjectsView
from .views.create_project import ProjectCreateView

urlpatterns = [
    path('new-project/', ProjectCreateView.as_view(), name='project_create'),
    path('get-projects/', GetAllProjectsView.as_view(), name='get_projects'),
    path('project/<int:project_id>/tasks/', GetTasksForProjectView.as_view(), name='task_list'),
    path('project/<int:project_id>/task/add/', TaskCreateView.as_view(), name='task_create'),
    path('project/<int:project_id>/task/<int:task_id>/change-status/', ChangeTaskStatusView.as_view(), name='change_task_status'),
]