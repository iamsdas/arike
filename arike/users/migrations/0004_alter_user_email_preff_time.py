# Generated by Django 3.2.12 on 2022-03-01 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220301_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_preff_time',
            field=models.TimeField(default=datetime.time(17, 57, 49, 955129)),
        ),
    ]