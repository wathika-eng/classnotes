# Generated by Django 4.2.7 on 2023-12-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_userrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userrequest',
            old_name='description',
            new_name='enquiry',
        ),
        migrations.RemoveField(
            model_name='userrequest',
            name='title',
        ),
        migrations.AddField(
            model_name='userrequest',
            name='yourcourse',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='yourschool',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
