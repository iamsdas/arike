# Generated by Django 3.2.12 on 2022-03-04 16:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0013_auto_20220304_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 16, 58, 46, 495174, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 16, 58, 46, 494130, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 16, 58, 46, 493018, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patientdisease',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 16, 58, 46, 495858, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 16, 58, 46, 496638, tzinfo=utc)),
        ),
    ]
