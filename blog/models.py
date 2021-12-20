from django.db import models


def file_path_dir(instance, filename):
    return 'uploads/project/{0}/{1}/{2}'.format(instance.project.id, instance.id, filename)


class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    thumbnail = models.FileField(upload_to='uploads/project/')

    def __str__(self):
        return self.title


class Event(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    thumbnail = models.FileField(upload_to=file_path_dir)
    project = models.ForeignKey(Project, on_delete=models.PROTECT,)

    def __str__(self):
        return self.title
