# Generated by Django 2.2.4 on 2022-06-29 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_project_App', '0003_remove_algorithm_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algorithm',
            name='desc',
            field=models.CharField(max_length=255),
        ),
    ]
