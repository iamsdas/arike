from django.contrib.auth import get_user_model
from django.forms import ModelForm
from arike.users.models import UserRoles
from arike.patients.models import FamilyMember, Patient, PatientDisease, Treatment

User = get_user_model()


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
            "reffered_nurse",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["reffered_nurse"].queryset = User.objects.filter(
            role=UserRoles.SECONDARY_NURSE
        )


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


class DiseaseHistoryForm(ModelForm):
    class Meta:
        model = PatientDisease
        fields = ["disease", "note"]


class TreatmentForm(ModelForm):
    class Meta:
        model = Treatment
        fields = ["care_type", "care_sub_type", "description"]
