from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from arike.facilities.forms import FacilityCreationForm
from arike.facilities.models import Facility


class GenericFacilityFormView(LoginRequiredMixin):
    form_class = FacilityCreationForm
    template_name = "facilities/form.html"
    success_url = "/facilities/list/"

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
    context_object_name = "facilities"

    def get_queryset(self):
        facilities = Facility.objects.all()
        search_filter = self.request.GET.get("search")
        if search_filter is not None:
            facilities = facilities.filter(name__icontains=search_filter)
        return facilities


class GenericFacilityDetailView(DetailView):
    model = Facility
    template_name = "facilities/detail.html"
