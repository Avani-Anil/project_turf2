# Generated by Django 4.1 on 2024-01-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='managertbl',
            name='password',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='managertbl',
            name='user',
            field=models.CharField(max_length=20, null=True),
        ),
    ]