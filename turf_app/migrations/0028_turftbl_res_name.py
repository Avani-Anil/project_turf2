# Generated by Django 5.0.1 on 2024-03-19 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf_app', '0027_rename_services_turftbl_sports_turftbl_res_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='turftbl',
            name='res_name',
            field=models.TextField(max_length=10, null=True),
        ),
    ]
