from django.shortcuts import render

# Create your views here.
from .models import Project, Event, Directory


def project_details(request, id):
    project = Project.objects.get(id=id)
    events = Event.objects.filter(project__id=project.id)
    context = {
        'project': project,
        'events': events
    }

    return render(request, "project/details.html", context)


def event_details(request, id):
    event = Event.objects.get(id=id)
    main_dir = Directory.objects.filter(event__id=event.id, parent_dir__id__isnull=True).first()
    context = {
        'event': event,
        'main_dir': main_dir
    }

    return render(request, "event/details.html", context)


def projects_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    return render(request, "project/list.html", context)
