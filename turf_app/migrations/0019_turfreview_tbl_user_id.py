# Generated by Django 5.0.1 on 2024-02-15 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turf_app', '0018_turfreview_tbl'),
    ]

    operations = [
        migrations.AddField(
            model_name='turfreview_tbl',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='turf_app.usertbl'),
        ),
    ]