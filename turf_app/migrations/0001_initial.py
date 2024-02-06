# Generated by Django 4.1 on 2024-01-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='managertbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20, null=True)),
                ('mname', models.CharField(max_length=20, null=True)),
                ('lname', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('dob', models.DateField(null=True)),
                ('phoneno', models.CharField(max_length=11, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('basicsal', models.CharField(max_length=20, null=True)),
                ('address', models.TextField(max_length=60, null=True)),
            ],
        ),
    ]