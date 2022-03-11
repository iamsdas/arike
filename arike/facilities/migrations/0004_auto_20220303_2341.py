# Generated by Django 3.2.12 on 2022-03-03 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0003_auto_20220303_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 3, 23, 41, 49, 763588)),
        ),
        migrations.AddField(
            model_name='facility',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 3, 23, 41, 49, 760338)),
        ),
        migrations.AddField(
            model_name='state',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]