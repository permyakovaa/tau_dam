# Generated by Django 4.2.2 on 2023-06-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_file_preview_compressed'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='compressing',
            field=models.BooleanField(default=False),
        ),
    ]
