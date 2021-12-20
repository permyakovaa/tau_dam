from django.contrib import admin
from .models import Post, Project, Event


class ProjectAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'created_at', 'thumbnail')


class EventAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'created_at', 'thumbnail', 'project')


admin.site.register(Post)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Event, EventAdmin)
