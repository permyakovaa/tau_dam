from django.shortcuts import render

from .models import Project, Event, Directory, File
from .forms import ProjectForm, EventForm, DirectoryForm, FileForm
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required


@login_required
def project_details(request, id):
    project = Project.objects.get(id=id)
    events = Event.objects.filter(project__id=project.id)
    context = {
        'project': project,
        'events': events
    }

    return render(request, "project/details.html", context)


@login_required
@permission_required('blog.add_project', raise_exception=True)
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


@login_required
@permission_required('blog.edit_project', raise_exception=True)
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


@login_required
@permission_required('blog.add_event', raise_exception=True)
def event_new(request, id):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        project = get_object_or_404(Project, id=id)

        if form.is_valid():
            event = form.save(commit=False)
            directory = Directory()
            directory.owner = request.user
            directory.created_at = timezone.now()
            directory.event = event

            event.owner = request.user
            event.created_at = timezone.now()
            event.project = project
            event.save()
            directory.save()
            return redirect('event_details', id=event.pk)
    else:
        form = EventForm()

    return render(request, 'event/form.html', {'form': form, 'type': 'new'})


@login_required
@permission_required('blog.edit_event', raise_exception=True)
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


@login_required
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


@login_required
@permission_required('blog.add_directory', raise_exception=True)
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


@login_required
@permission_required('blog.add_file', raise_exception=True)
def file_new(request, dir_id):
    directory = get_object_or_404(Directory, id=dir_id)
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.title = file.file
            file.owner = request.user
            file.created_at = timezone.now()
            file.parent_dir = directory
            file.save()

            return JsonResponse({'status': 'ok'})

    return JsonResponse({'status': 'error'})


@login_required
@permission_required('blog.delete_file', raise_exception=True)
def file_remove(request, id):
    file = get_object_or_404(File, id=id)
    dir_id = file.parent_dir.id
    event_id = file.parent_dir.event.id

    file.delete()

    return redirect('dir_details', id=event_id, dir_id=dir_id)


@login_required
def projects_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    return render(request, "project/list.html", context)
