# Generated by Django 3.0.4 on 2020-03-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_patientpath_paths'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientpath',
            name='paths',
        ),
        migrations.AddField(
            model_name='patient',
            name='paths',
            field=models.TextField(null=True),
        ),
    ]
