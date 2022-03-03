from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from arike.patients.forms import (
    DiseaseHistoryForm,
    FamilyMemberForm,
    PatientForm,
    TreatmentForm,
)
from arike.patients.models import FamilyMember, Patient, PatientDisease, Treatment
from arike.facilities.models import Ward
from arike.visits.models import VisitDetails
from arike.users.models import UserRoles


class GenericPatientFormView(LoginRequiredMixin):
    form_class = PatientForm
    template_name = "patients/form.html"
    success_url = "/patient/list/"

    def get_queryset(self):
        user = self.request.user
        district = user.facility.ward.lsg_body.district
        patients = Patient.objects.filter(
            facility__ward__lsg_body__district=district, deleted=False
        )
        if user.role == UserRoles.SECONDARY_NURSE:
            patients.union(Patient.objects.filter(reffered_nurse=user))
        return patients


class PatientCreateView(GenericPatientFormView, CreateView):
    pass


class PatientUpdateView(GenericPatientFormView, UpdateView):
    pass


class PatientDeleteView(GenericPatientFormView, DeleteView):
    def delete(self, request: HttpRequest, *args: str, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.deleted = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class GenericFamilyMemberFormView(LoginRequiredMixin):
    form_class = FamilyMemberForm
    template_name = "family/form.html"
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_queryset(self):
        patient_pk = self.kwargs["pk"]
        return FamilyMember.objects.filter(patient__pk=patient_pk, deleted=False)

    def get_success_url(self):
        return reverse_lazy("patients:family", kwargs={"pk": self.kwargs["pk"]})


class MemberCreateView(GenericFamilyMemberFormView, CreateView):
    pass


class MemberUpdateView(GenericFamilyMemberFormView, UpdateView):
    pass


class MemberDeleteView(GenericFamilyMemberFormView, DeleteView):
    pass


class GenericDiseaseFormView(LoginRequiredMixin):
    form_class = DiseaseHistoryForm
    template_name = "disease/form.html"
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_queryset(self):
        patient_pk = self.kwargs["pk"]
        return PatientDisease.objects.filter(patient__pk=patient_pk)

    def get_success_url(self):
        return reverse_lazy("patients:disease", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.patient = Patient.objects.get(pk=self.kwargs["pk"])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class DiseaseCreateView(GenericDiseaseFormView, CreateView):
    pass


class DiseaseUpdateView(GenericDiseaseFormView, UpdateView):
    pass


class DiseaseDeleteView(GenericDiseaseFormView, DeleteView):
    pass


class GenericTreatmentFormView(LoginRequiredMixin):
    form_class = TreatmentForm
    template_name = "treatment/form.html"
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_queryset(self):
        patient_pk = self.kwargs["pk"]
        return Treatment.objects.filter(patient__pk=patient_pk)

    def get_success_url(self):
        return reverse_lazy("patients:treatments", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.patient = Patient.objects.get(pk=self.kwargs["pk"])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class TreatmentCreateView(GenericTreatmentFormView, CreateView):
    pass


class TreatmentUpdateView(GenericTreatmentFormView, UpdateView):
    pass


class TreatmentDeleteView(GenericTreatmentFormView, DeleteView):
    pass


class PatientListVeiw(LoginRequiredMixin, ListView):
    model = Patient
    template_name = "patients/list.html"
    context_object_name = "patients"

    def get_queryset(self):
        patients = Patient.objects.all()
        search_filter = self.request.GET.get("search")
        ward_filter = self.request.GET.get("ward")
        type_filter = self.request.GET.get("type")
        if search_filter is not None:
            patients = patients.filter(full_name__icontains=search_filter)
        if ward_filter is not None:
            patients = patients.filter(facility__ward__name=ward_filter)
        if type_filter is not None:
            patients = patients.filter(facility__kind=type_filter)
        return patients

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["wards"] = list(Ward.objects.values_list("name", flat=True))
        return ctx


class FamilyListVeiw(LoginRequiredMixin, ListView):
    model = FamilyMember
    template_name = "family/list.html"
    context_object_name = "members"

    def get_queryset(self):
        family_members = FamilyMember.objects.all()
        search_filter = self.request.GET.get("search")
        if search_filter is not None:
            family_members = family_members.filter(full_name__icontains=search_filter)
        return family_members

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["patient"] = Patient.objects.get(pk=self.kwargs["pk"])
        return ctx


class VisitListVeiw(LoginRequiredMixin, ListView):
    model = VisitDetails
    template_name = "visit_details/list.html"
    context_object_name = "visits"

    def get_queryset(self):
        return VisitDetails.objects.filter(schedule__patient__pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["patient"] = Patient.objects.get(pk=self.kwargs["pk"])
        return ctx


class DiseaseListVeiw(LoginRequiredMixin, ListView):
    model = PatientDisease
    template_name = "disease/list.html"
    context_object_name = "diseases"

    def get_queryset(self):
        diseases = PatientDisease.objects.filter(patient__pk=self.kwargs["pk"])
        return diseases

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["patient"] = Patient.objects.get(pk=self.kwargs["pk"])
        return ctx


class TreatmentsListVeiw(LoginRequiredMixin, ListView):
    model = Treatment
    template_name = "treatment/list.html"
    context_object_name = "treatments"

    def get_queryset(self):
        treatments = Treatment.objects.filter(patient__pk=self.kwargs["pk"])
        return treatments

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["patient"] = Patient.objects.get(pk=self.kwargs["pk"])
        return ctx


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = "patients/detail.html"


class VisitDetailsDetailView(LoginRequiredMixin, DetailView):
    model = VisitDetails
    template_name = "visit_details/details.html"
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["patient"] = Patient.objects.get(pk=self.kwargs["pk"])
        return ctx
