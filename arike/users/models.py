from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from arike.facilities.models import Facility


class UserRoles(models.TextChoices):
    DISTRICT_ADMIN = "District Admin"
    PRIMARY_NURSE = "Primary Nurse"
    SECONDARY_NURSE = "Secondary Nurse"


class User(AbstractUser):
    """
    Default custom user model for Arike.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    role = models.CharField(
        max_length=20, choices=UserRoles.choices, default=UserRoles.DISTRICT_ADMIN
    )
    phone = models.CharField(max_length=12, unique=True)
    is_verified = models.BooleanField(default=False, blank=True)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, null=True)
    email_preff_time = models.TimeField(default=datetime.now().time())
    email_last_sent = models.DateField(default=datetime.now().date())
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
