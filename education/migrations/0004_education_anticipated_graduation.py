# Generated by Django 4.1.7 on 2023-05-14 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_alter_education_courses_alter_education_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='anticipated_graduation',
            field=models.BooleanField(default=False),
        ),
    ]
