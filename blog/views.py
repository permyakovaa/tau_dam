from django.shortcuts import render

# Create your views here.
from .models import Post, Project, Event


def blog_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, "project/list.html", context)


def project_details(request, id):
    project = Project.objects.get(id=id)
    events = Event.objects.filter(project__id=project.id)
    context = {
        'project': project,
        'events': events
    }

    return render(request, "project/details.html", context)


def projects_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    return render(request, "project/list.html", context)
