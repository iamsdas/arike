from django.forms import ModelForm
from arike.visits.models import VisitDetails, VisitSchedule, TreatmentNote


class VisitScheduleForm(ModelForm):
    class Meta:
        model = VisitSchedule
        fields = ["patient", "date", "time", "duration"]


class VisitDetailsForm(ModelForm):
    class Meta:
        model = VisitDetails
        fields = [
            "blood_pressure",
            "pulse",
            "sugar",
            "mouth_hygiene",
            "public_hygiene",
            "systemic_examination",
            "patient_at_peace",
            "pain",
            "symptoms",
            "note",
            "schedule",
        ]


class TreatmentNoteForm(ModelForm):
    class Meta:
        model = TreatmentNote
        fields = ["note"]
