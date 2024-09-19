from ..models import Project

class ProjectService:
    @staticmethod
    def get_all_projects():
        return Project.objects.all()