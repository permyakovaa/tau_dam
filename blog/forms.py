from django import forms
from .models import Project, Event
from django.utils.translation import gettext as _


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'created_at', 'thumbnail')

        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'created_at': _('Created At'),
            'thumbnail': _('Thumbnail')
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'created_at', 'thumbnail', 'project')

        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'created_at': _('Created At'),
            'thumbnail': _('Thumbnail'),
            'project': _('Project'),
        }