# Generated by Django 3.2.12 on 2022-03-01 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_email_preff_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_preff_time',
            field=models.TimeField(default=datetime.time(18, 11, 51, 357632)),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]