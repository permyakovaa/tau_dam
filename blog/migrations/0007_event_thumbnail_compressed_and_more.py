# Generated by Django 4.2.2 on 2023-06-16 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_file_compressing'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='thumbnail_compressed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='thumbnail_compressed',
            field=models.BooleanField(default=False),
        ),
    ]