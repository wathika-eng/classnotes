# Generated by Django 4.2.7 on 2023-12-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_note_unique_together_note_unit_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='unit',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='unit',
            name='sem',
            field=models.CharField(choices=[('1', 'First Semester'), ('2', 'Second Semester')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='year_of_study',
            field=models.CharField(choices=[('1', 'First Year'), ('2', 'Second Year'), ('3', 'Third Year'), ('4', 'Fourth Year')], max_length=20, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('name', 'department')},
        ),
        migrations.AlterUniqueTogether(
            name='unit',
            unique_together={('name', 'course', 'year_of_study')},
        ),
        migrations.RemoveField(
            model_name='course',
            name='sem',
        ),
        migrations.RemoveField(
            model_name='course',
            name='year_of_study',
        ),
    ]