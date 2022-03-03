# Generated by Django 3.2.12 on 2022-03-03 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20220302_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_last_sent',
            field=models.DateField(default=datetime.date(2022, 3, 3)),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_preff_time',
            field=models.TimeField(default=datetime.time(15, 40, 13, 465282)),
        ),
    ]
