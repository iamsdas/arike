from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from arike.facilities.models import Facility

User = get_user_model()


class GenderChoice(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class FamilyRelation(models.TextChoices):
    SISTER = "Sister"
    BROTHER = "Brother"
    FATHER = "Father"
    MOTHER = "Mother"


class Patient(models.Model):
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    expired_time = models.DateField(null=True, blank=True)
    address = models.TextField()
    landmark = models.CharField(max_length=100)
    phone = models.CharField(max_length=12, unique=True)
    emergency_phone_number = models.CharField(max_length=12, unique=True)
    gender = models.CharField(max_length=20, choices=GenderChoice.choices)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    reffered_nurse = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL
    )
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(null=True)

    def save(self):
        self.updated_at = timezone.now()
        return super().save()

    def __str__(self):
        return self.full_name


class FamilyMember(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12, unique=True)
    date_of_birth = models.DateField()
    email = models.CharField(max_length=50)
    relation = models.CharField(max_length=20, choices=FamilyRelation.choices)
    address = models.TextField()
    education = models.CharField(max_length=20)
    occupation = models.CharField(max_length=10)
    remarks = models.TextField()
    is_primary = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(null=True)

    def save(self):
        self.updated_at = timezone.now()
        return super().save()


class Disease(models.Model):
    name = models.CharField(max_length=20)
    icds_code = models.CharField(max_length=10, unique=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(null=True)

    def save(self):
        self.updated_at = timezone.now()
        return super().save()

    def __str__(self):
        return self.name


class PatientDisease(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    note = models.TextField()
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(null=True)

    def save(self):
        self.updated_at = timezone.now()
        return super().save()


class Treatment(models.Model):
    description = models.TextField()
    care_type = models.CharField(max_length=20)
    care_sub_type = models.CharField(max_length=20)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(null=True)

    def save(self):
        self.updated_at = timezone.now()
        return super().save()
