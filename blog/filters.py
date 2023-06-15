import django_filters
from .models import Project, Event
from django.utils.translation import gettext as _

class ProjectFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label=_('Filter by title'))

    class Meta:
        model = Project
        fields = ['title']

class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label=_('Filter by title'))

    class Meta:
        model = Event
        fields = ['title']