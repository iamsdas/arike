from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from arike.facilities.forms import FacilityCreationForm
from arike.facilities.models import Facility
from django.views.generic import ListView, View


class GenericFacilityFormView(LoginRequiredMixin):
    form_class = FacilityCreationForm
    template_name = "facilities/form.html"
    success_url = "/"

    def get_queryset(self):
        return Facility.objects.all()


class FacilityCreateView(GenericFacilityFormView, CreateView):
    pass


class FacilityUpdateView(GenericFacilityFormView, UpdateView):
    pass


class FacilityDeleteView(GenericFacilityFormView, DeleteView):
    pass


class GenericFacilityListVeiw(ListView, LoginRequiredMixin):
    model = Facility
    template_name = "facilities/list.html"

    def get_queryset(self):
        return Facility.objects.all()
