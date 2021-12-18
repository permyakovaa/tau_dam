from django.urls import path
from .views import blog_details, projects_list

urlpatterns = [
    path('', projects_list),
    path('<id>/', blog_details)
]