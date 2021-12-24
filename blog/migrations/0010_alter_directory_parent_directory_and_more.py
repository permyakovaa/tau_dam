# Generated by Django 4.0 on 2021-12-21 17:33

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_directory_parent_directory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directory',
            name='parent_directory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.directory'),
        ),
        migrations.AlterField(
            model_name='directory',
            name='thumbnail',
            field=models.FileField(upload_to=blog.models.dir_thumb_path_dir),
        ),
    ]