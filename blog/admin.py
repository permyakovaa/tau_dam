from django.contrib import admin
from .models import Post, Project


class ProjectAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'created_at', 'thumbnail')


admin.site.register(Post)
admin.site.register(Project, ProjectAdmin)