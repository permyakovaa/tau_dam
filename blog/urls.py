from django.urls import path
from .views import project_details, project_new, project_edit, projects_list, event_details

urlpatterns = [
    path('', projects_list),
    path('project/new/', project_new, name='project_new'),
    path('project/edit/<int:id>/', project_edit, name='project_edit'),
    path('project/<int:id>/', project_details, name='project_details'),
    path('event/<int:id>/', event_details, name='event_details')
]