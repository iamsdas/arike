# Generated by Django 3.2.12 on 2022-03-03 18:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0011_auto_20220303_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 3, 18, 48, 47, 163914, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='disease',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='familymember',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 3, 18, 48, 47, 162749, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='familymember',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 3, 18, 48, 47, 161443, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='patient',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='patientdisease',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 3, 18, 48, 47, 164656, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='patientdisease',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 3, 18, 48, 47, 165537, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='treatment',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='treatmentnote',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 3, 18, 48, 47, 166418, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='treatmentnote',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
