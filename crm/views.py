from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project

def project_list(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    
    projects = Project.objects.all()
    return render(request, 'crm/project_list.html', {'projects': projects, 'form': form})