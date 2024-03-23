# Generated by Django 5.0.1 on 2024-03-22 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf_app', '0031_turftbl_district'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingtbl',
            name='amenities',
        ),
        migrations.RemoveField(
            model_name='bookingtbl',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='bookingtbl',
            name='email',
        ),
        migrations.RemoveField(
            model_name='bookingtbl',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='bookingtbl',
            name='loc',
        ),
        migrations.RemoveField(
            model_name='bookingtbl',
            name='services',
        ),
        migrations.RemoveField(
            model_name='bookingtbl',
            name='timing',
        ),
        migrations.RemoveField(
            model_name='bookingtbl',
            name='tname',
        ),
        migrations.RemoveField(
            model_name='resource_tbl',
            name='turf_name',
        ),
        migrations.AddField(
            model_name='bookingtbl',
            name='res_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='turf_app.resource_tbl'),
        ),
        migrations.AddField(
            model_name='bookingtbl',
            name='turf_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='turf_app.turftbl'),
        ),
        migrations.AddField(
            model_name='resource_tbl',
            name='turf_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='turf_app.turftbl'),
        ),
        migrations.AddField(
            model_name='turfreview_tbl',
            name='review',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='usertbl',
            name='district',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='turfreview_tbl',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='turftbl',
            name='district',
            field=models.CharField(max_length=20, null=True),
        ),
    ]