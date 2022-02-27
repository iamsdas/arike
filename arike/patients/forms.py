from django.forms import ModelForm

from arike.patients.models import FamilyMember, Patient


class PatientForm(ModelForm):
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


class FamilyMemberForm(ModelForm):
    class Meta:
        model = FamilyMember
        fields = [
            "full_name",
            "phone",
            "date_of_birth",
            "email",
            "relation",
            "address",
            "education",
            "occupation",
            "remarks",
            "patient",
        ]
