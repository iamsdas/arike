from django.forms import ModelForm

from arike.facilities.models import Facility


class FacilityCreationForm(ModelForm):
    class Meta:
        model = Facility
        fields = ["name", "kind", "address", "pincode", "phone", "ward"]
