from django.shortcuts import render

from .models import Project, Event, Directory
from .forms import ProjectForm, EventForm, DirectoryForm
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone


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
            project.owner = request.user
            project.created_at = timezone.now()
            project.save()
            return redirect('project_details', id=project.pk)
    else:
        form = ProjectForm()

    return render(request, 'project/form.html', {'form': form, 'type': 'new'})


def project_edit(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('project_details', id=project.pk)
    else:
        form = ProjectForm(instance=project)

    return render(request, 'project/form.html', {'form': form, 'type': 'edit'})


def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            event.created_at = timezone.now()
            event.save()
            return redirect('event_details', id=event.pk)
    else:
        form = EventForm()

    return render(request, 'event/form.html', {'form': form, 'type': 'new'})


def event_edit(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('event_details', id=event.pk)
    else:
        form = EventForm(instance=event)

    return render(request, 'event/form.html', {'form': form, 'type': 'edit'})


def event_details(request, id, dir_id=None):
    event = Event.objects.get(id=id)

    if dir_id is not None:
        current_dir = get_object_or_404(Directory, id=dir_id, event=event.pk)
    else:
        current_dir = Directory.objects.filter(event__id=event.id, parent_dir__id__isnull=True).first()

    context = {
        'event': event,
        'current_dir': current_dir
    }

    return render(request, "event/details.html", context)


def directory_new(request, event_id, parent_dir_id):
    event = get_object_or_404(Event, id=event_id)
    parent_dir = get_object_or_404(Directory, id=parent_dir_id)
    if request.method == "POST":
        form = DirectoryForm(request.POST)
        if form.is_valid():
            directory = form.save(commit=False)
            directory.owner = request.user
            directory.created_at = timezone.now()
            directory.event = event
            directory.parent_dir = parent_dir

            directory.save()
            return redirect('dir_details', id=event.pk, dir_id=parent_dir.id)
    else:
        form = DirectoryForm

    return render(request, 'directory/form.html', {'form': form, 'type': 'new'})


def projects_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    return render(request, "project/list.html", context)
