from django.db import models


class FacilityType(models.TextChoices):
    PHC = "PHC"
    CHC = "CHC"


class LSGType(models.TextChoices):
    GRAM_PANCHAYAT = "Gram Panchayat"
    MUNICIPALITY = "Municipality"


class State(models.Model):
    name = models.CharField(max_length=30)


class District(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE)


class LocalBody(models.Model):
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=50, choices=LSGType.choices)
    lsg_body_code = models.CharField(max_length=20)
    district = models.ForeignKey(District, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Ward(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField(unique=True)
    lsg_body = models.ForeignKey(LocalBody, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Facility(models.Model):
    kind = models.CharField(
        max_length=3, choices=FacilityType.choices, default=FacilityType.PHC
    )
    name = models.CharField(max_length=100)
    address = models.TextField()
    pincode = models.IntegerField()
    phone = models.IntegerField()
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
