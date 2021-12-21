from django.urls import path
from .views import project_details, projects_list, event_details

urlpatterns = [
    path('', projects_list),
    path('project/<id>/', project_details, name='project_details'),
    path('event/<id>/', event_details, name='event_details')
]