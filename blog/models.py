import os
from django.contrib.auth.models import User
from django.db import models


def file_path_dir(instance, filename):
    return 'project/{0}/{1}'.format(instance.parent_dir.id, filename)


class Project(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    thumbnail = models.FileField(upload_to='project/preview/')
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    thumbnail_compressed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def thumb_url(self):
        thumb_url = self.thumbnail.name

        if (self.thumbnail_compressed):
            name, extension = os.path.splitext(self.thumbnail.name)

            thumb_url = name + '_preview' + extension

        return thumb_url
    

class Event(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    thumbnail = models.FileField(upload_to='project/preview/')
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    thumbnail_compressed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def thumb_url(self):
        thumb_url = self.thumbnail.name

        if (self.thumbnail_compressed):
            name, extension = os.path.splitext(self.thumbnail.name)

            thumb_url = name + '_preview' + extension

        return thumb_url

class Directory(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='directories')
    parent_dir = models.ForeignKey('Directory', on_delete=models.PROTECT, null=True, blank=True, related_name='child_dirs')
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def breadcrumbs(self):
        breadcrumbs = []
        parent_dir = self.parent_dir

        while parent_dir is not None:
            if parent_dir.title != '':
                breadcrumbs.append({'id': parent_dir.id, 'title': parent_dir.title})

            parent_dir = parent_dir.parent_dir

        return reversed(breadcrumbs)

    def __str__(self):
        return self.event.title + ': ' + self.title


class File(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    file = models.FileField(upload_to=file_path_dir)
    preview_file = models.FileField(upload_to=file_path_dir, null=True, blank=True)
    preview_compressed = models.BooleanField()
    compressing = models.BooleanField(default=False)
    size = models.BigIntegerField()
    parent_dir = models.ForeignKey(Directory, on_delete=models.PROTECT, related_name='files')
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension

    def name(self):
        name, extension = os.path.splitext(self.file.name)
        return name

    def is_image(self):
        return self.extension().lower() in ['.png', '.jpeg', '.jpg']

    def is_video(self):
        return self.extension().lower() in ['.mp4', '.avi', '.webm', '.mov']

    def is_pdf(self):
        return self.extension().lower() in ['.pdf']

    def __str__(self):
        return self.title