# Generated by Django 3.2.12 on 2022-03-03 18:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0004_auto_20220303_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 3, 18, 14, 36, 195288, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='state',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 3, 18, 14, 36, 191999, tzinfo=utc)),
        ),
    ]
