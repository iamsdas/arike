from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

from arike.facilities.models import Facility

User = get_user_model()


class GenderChoice(models.TextChoices):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"


class FamilyRelation(models.TextChoices):
    SISTER = "S"
    BROTHER = "B"
    FATHER = "F"
    MOTHER = "M"


class Hygiene(models.TextChoices):
    GOOD = "good"
    POOR = "poor"
    OK = "ok"


class Symptoms(models.TextChoices):
    FEVER = "fever"
    CAUGHING = "caughing"


class Patient(models.Model):
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    expired_time = models.DateField(null=True, blank=True)
    address = models.TextField()
    landmark = models.CharField(max_length=100)
    phone = models.IntegerField(unique=True)
    emergency_phone_number = models.IntegerField(unique=True)
    gender = models.CharField(max_length=1, choices=GenderChoice.choices)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class FamilyMember(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.IntegerField(unique=True)
    date_of_birth = models.DateField()
    email = models.CharField(max_length=50)
    relation = models.CharField(max_length=1, choices=FamilyRelation.choices)
    address = models.TextField()
    education = models.CharField(max_length=20)
    occupation = models.CharField(max_length=10)
    remarks = models.TextField()
    is_primary = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Disease(models.Model):
    name = models.CharField(max_length=20)
    icds_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class PatientDisease(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    note = models.TextField()


class VisitSchedule(models.Model):
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    duration = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    nurse = models.ForeignKey(User, on_delete=models.CASCADE)


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


class Treatment(models.Model):
    description = models.TextField()
    care_type = models.CharField(max_length=20)
    care_sub_type = models.CharField(max_length=20)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class TreatmentNote(models.Model):
    note = models.TextField()
    description = models.TextField()
    care_type = models.CharField(max_length=10)
    care_sub_type = models.CharField(max_length=20)
    treatment = models.OneToOneField(Treatment, on_delete=models.CASCADE)
