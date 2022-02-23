from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices):
    DISTRICT_ADMIN = "DA"
    PRIMARY_NURSE = "PN"
    SECONDARY_NURSE = "SN"


class User(AbstractUser):
    """
    Default custom user model for Arike.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    role = models.CharField(
        max_length=2, choices=UserRoles.choices, default=UserRoles.DISTRICT_ADMIN
    )
    phone = models.CharField(max_length=16, unique=True, null=True)
    is_verified = models.BooleanField(default=False)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
