# Generated by Django 4.1.7 on 2023-05-14 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_alter_education_courses_alter_education_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='courses',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='education'),
        ),
    ]
