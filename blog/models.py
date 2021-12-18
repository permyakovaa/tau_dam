from django.db import models


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    objects = None
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField()
    thumbnail = models.FileField(upload_to='uploads/project/')

    def __str__(self):
        return self.title
