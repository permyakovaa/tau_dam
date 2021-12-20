from django.urls import path
from .views import project_details, projects_list

urlpatterns = [
    path('', projects_list),
    path('project/<id>/', project_details, name='project_details')
]