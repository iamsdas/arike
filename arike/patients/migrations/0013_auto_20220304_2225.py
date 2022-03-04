# Generated by Django 3.2.12 on 2022-03-04 16:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0012_auto_20220304_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 16, 55, 25, 321671, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 16, 55, 25, 320481, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 16, 55, 25, 319167, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patientdisease',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 16, 55, 25, 322422, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 16, 55, 25, 323307, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='TreatmentNote',
        ),
    ]
