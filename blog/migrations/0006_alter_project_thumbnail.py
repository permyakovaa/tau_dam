# Generated by Django 4.0 on 2021-12-18 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.FileField(upload_to='uploads/project/'),
        ),
    ]