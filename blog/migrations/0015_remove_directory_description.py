# Generated by Django 4.0 on 2021-12-25 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_delete_post_directory_owner_event_owner_file_owner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directory',
            name='description',
        ),
    ]