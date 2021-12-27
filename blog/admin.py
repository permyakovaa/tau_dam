from django.contrib import admin
from .models import Project, Event, Directory, File


class ProjectAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'created_at', 'thumbnail')


class EventAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'created_at', 'thumbnail', 'project')


class DirectoryAdmin(admin.ModelAdmin):
    fields = ('title', 'created_at', 'event', 'parent_dir')


class FileAdmin(admin.ModelAdmin):
    fields = ('title', 'created_at', 'file', 'parent_dir')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Directory, DirectoryAdmin)
admin.site.register(File, FileAdmin)
