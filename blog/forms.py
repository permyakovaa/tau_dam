from django import forms
from .models import Project, Event, Directory, File
from django.utils.translation import gettext as _


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'thumbnail')

        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'thumbnail': _('Thumbnail')
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'thumbnail', 'project')

        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'thumbnail': _('Thumbnail'),
            'project': _('Project'),
        }


class DirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = ('title',)

        labels = {
            'title': _('Title')
        }


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file',)
