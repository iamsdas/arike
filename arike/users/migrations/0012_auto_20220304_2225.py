# Generated by Django 3.2.12 on 2022-03-04 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_user_email_preff_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_last_sent',
            field=models.DateField(default=datetime.date(2022, 3, 4)),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_preff_time',
            field=models.TimeField(default=datetime.time(16, 55, 25, 314399)),
        ),
    ]