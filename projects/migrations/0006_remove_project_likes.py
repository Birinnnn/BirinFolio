# Generated by Django 4.1.7 on 2023-05-13 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_remove_project_user_project_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='likes',
        ),
    ]
