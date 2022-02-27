from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from arike.patients.forms import PatientCreationForm
from arike.patients.models import Patient


class GenericPatientFormView(LoginRequiredMixin):
    form_class = PatientCreationForm
    template_name = "patients/form.html"
    success_url = "/patient/list/"

    def get_queryset(self):
        return Patient.objects.all()


class PatientCreateView(GenericPatientFormView, CreateView):
    pass


class PatientUpdateView(GenericPatientFormView, UpdateView):
    pass


class PatientDeleteView(GenericPatientFormView, DeleteView):
    pass


class GenericPatientListVeiw(ListView, LoginRequiredMixin):
    model = Patient
    template_name = "patients/list.html"
    context_object_name = "patients"

    def get_queryset(self):
        patients = Patient.objects.all()
        search_filter = self.request.GET.get("search")
        if search_filter is not None:
            patients = patients.filter(full_name__icontains=search_filter)
        return patients


class GenericPatientDetailView(DetailView):
    model = Patient
    template_name = "patients/detail.html"
