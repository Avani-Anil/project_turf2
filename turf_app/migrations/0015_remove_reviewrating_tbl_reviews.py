# Generated by Django 5.0.1 on 2024-02-14 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turf_app', '0014_rename_review_reviewrating_tbl_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewrating_tbl',
            name='reviews',
        ),
    ]
