from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'projects/home.html')

def viewProj(request):
    projects = Project.objects.all()
    return render(request,'projects/viewProjects.html', {'projects': projects})