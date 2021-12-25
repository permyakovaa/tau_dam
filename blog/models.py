from django.contrib.auth.models import User
from django.db import models


def file_path_dir(instance, filename):
    return 'uploads/project/{0}/{1}/{2}'.format(instance.project.id, instance.id, filename)


def project_path_dir(instance, filename):
    return 'uploads/project/{0}/{1}/{2}'.format(instance.parent_dir.id, instance.id, filename)


def dir_thumb_path_dir(instance, filename):
    return 'uploads/project/{0}/{1}/{2}'.format(instance.event.project.id, instance.id, filename)


class Project(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    thumbnail = models.FileField(upload_to='uploads/project/')
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Event(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    thumbnail = models.FileField(upload_to=file_path_dir)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Directory(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    thumbnail = models.FileField(upload_to=dir_thumb_path_dir)
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='directories')
    parent_dir = models.ForeignKey('Directory', on_delete=models.PROTECT, null=True, blank=True, related_name='child_dirs')
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.event.title + ': ' + self.title


class File(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    file = models.FileField(upload_to=project_path_dir)
    parent_dir = models.ForeignKey(Directory, on_delete=models.PROTECT, related_name='files')
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title