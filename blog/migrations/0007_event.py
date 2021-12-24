# Generated by Django 4.0 on 2021-12-20 17:01

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_project_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('thumbnail', models.FileField(upload_to=blog.models.file_path_dir)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.project')),
            ],
        ),
    ]