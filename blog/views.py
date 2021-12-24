from django.shortcuts import render

from .models import Project, Event, Directory
from .forms import ProjectForm
from django.shortcuts import redirect, get_object_or_404


def project_details(request, id):
    project = Project.objects.get(id=id)
    events = Event.objects.filter(project__id=project.id)
    context = {
        'project': project,
        'events': events
    }

    return render(request, "project/details.html", context)


def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            # post.author = request.user
            project.save()
            return redirect('project_details', id=project.pk)
    else:
        form = ProjectForm()

    return render(request, 'project/new.html', {'form': form})


def project_edit(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            # post.author = request.user
            project.save()
            return redirect('project_details', id=project.pk)
    else:
        form = ProjectForm(instance=project)

    return render(request, 'project/new.html', {'form': form})


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
