# Generated by Django 5.0.1 on 2024-03-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf_app', '0032_remove_bookingtbl_amenities_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingtbl',
            name='res_id',
        ),
        migrations.RemoveField(
            model_name='bookingtbl',
            name='turf_id',
        ),
        migrations.AddField(
            model_name='bookingtbl',
            name='loc',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='bookingtbl',
            name='timing',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='bookingtbl',
            name='tname',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
