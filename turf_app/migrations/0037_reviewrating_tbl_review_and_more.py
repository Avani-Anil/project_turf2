# Generated by Django 5.0.1 on 2024-03-22 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf_app', '0036_alter_turftbl_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrating_tbl',
            name='review',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='reviewrating_tbl',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]