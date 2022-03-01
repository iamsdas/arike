from django.forms import ModelForm
from arike.visits.models import VisitSchedule


class VisitScheduleForm(ModelForm):
    class Meta:
        model = VisitSchedule
        fields = ["patient", "date", "time", "duration"]
