# Generated by Django 4.1 on 2024-01-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf_app', '0003_turftbl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turftbl',
            name='loc',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
