# Generated by Django 5.0.1 on 2024-02-14 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf_app', '0015_remove_reviewrating_tbl_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrating_tbl',
            name='fname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='reviewrating_tbl',
            name='rating',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
