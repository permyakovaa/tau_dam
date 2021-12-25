from django.urls import path
from .views import project_details, project_new, project_edit, projects_list, event_details
from .views import event_new, event_edit, directory_new, file_new

urlpatterns = [
    path('', projects_list),
    path('project/new/', project_new, name='project_new'),
    path('project/edit/<int:id>/', project_edit, name='project_edit'),
    path('project/<int:id>/', project_details, name='project_details'),
    path('event/new/', event_new, name='event_new'),
    path('event/edit/<int:id>/', event_edit, name='event_edit'),
    path('event/<int:id>/dir/<int:dir_id>', event_details, name='dir_details'),
    path('event/<int:id>', event_details, name='event_details'),
    path('directory/new/<int:event_id>/<int:parent_dir_id>', directory_new, name='directory_new'),
    path('directory/<int:dir_id>/new_file/', file_new, name='file_new'),
]