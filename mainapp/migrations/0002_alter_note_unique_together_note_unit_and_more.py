# Generated by Django 4.2.7 on 2023-12-04 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='note',
            unique_together={('title', 'file')},
        ),
        migrations.AddField(
            model_name='note',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='mainapp.unit'),
        ),
        migrations.AlterUniqueTogether(
            name='note',
            unique_together={('title', 'unit', 'file'), ('title', 'unit'), ('unit', 'file'), ('title', 'file')},
        ),
        migrations.RemoveField(
            model_name='note',
            name='unit_topic',
        ),
    ]
