# Generated by Django 3.2.12 on 2022-03-03 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20220303_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_preff_time',
            field=models.TimeField(default=datetime.time(15, 48, 17, 196769)),
        ),
    ]