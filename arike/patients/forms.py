from django.forms import ModelForm

from arike.patients.models import Patient


class PatientCreationForm(ModelForm):
    class Meta:
        model = Patient
        fields = [
            "full_name",
            "date_of_birth",
            "expired_time",
            "address",
            "landmark",
            "phone",
            "emergency_phone_number",
            "gender",
            "facility",
        ]
