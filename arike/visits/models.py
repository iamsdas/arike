from django.contrib.auth import get_user_model
from django.db import models

from arike.patients.models import Patient

User = get_user_model()


class Hygiene(models.TextChoices):
    GOOD = "good"
    POOR = "poor"
    OK = "ok"


class Symptoms(models.TextChoices):
    FEVER = "fever"
    CAUGHING = "caughing"


class VisitSchedule(models.Model):
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    duration = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    nurse = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} at {self.time}"


class VisitDetails(models.Model):
    blood_pressure = models.IntegerField()
    pulse = models.IntegerField()
    sugar = models.FloatField()
    mouth_hygiene = models.CharField(max_length=4, choices=Hygiene.choices)
    public_hygiene = models.CharField(max_length=4, choices=Hygiene.choices)
    systemic_examination = models.TextField()
    patient_at_peace = models.BooleanField()
    pain = models.BooleanField()
    symptoms = models.CharField(max_length=20, choices=Symptoms.choices)
    note = models.TextField()
    schedule = models.OneToOneField(VisitSchedule, on_delete=models.CASCADE)
