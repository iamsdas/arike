# Generated by Django 3.2.12 on 2022-03-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0010_patient_reffered_nurse'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='familymember',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patientdisease',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='treatment',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='treatmentnote',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
