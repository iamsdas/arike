# Generated by Django 3.2.12 on 2022-03-12 13:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0009_auto_20220304_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 13, 42, 45, 775102, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='localbody',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 13, 42, 45, 774451, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='state',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 13, 42, 45, 773814, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ward',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 13, 42, 45, 774777, tzinfo=utc)),
        ),
    ]
