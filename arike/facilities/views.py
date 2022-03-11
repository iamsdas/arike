from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from arike.facilities.forms import FacilityCreationForm
from arike.facilities.models import Facility, Ward
from arike.users.models import UserRoles


class AdminAuthMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == UserRoles.DISTRICT_ADMIN


class GenericFacilityFormView(AdminAuthMixin):
    form_class = FacilityCreationForm
    template_name = "facilities/form.html"

    def get_queryset(self):
        return Facility.objects.filter(deleted=False)

    def get_success_url(self):
        return reverse_lazy("facilities:list")


class FacilityCreateView(GenericFacilityFormView, CreateView):
    pass


class FacilityUpdateView(GenericFacilityFormView, UpdateView):
    pass


class FacilityDeleteView(GenericFacilityFormView, DeleteView):
    def delete(self, request: HttpRequest, *args: str, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.deleted = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class GenericFacilityListVeiw(AdminAuthMixin, ListView):
    model = Facility
    template_name = "facilities/list.html"
    context_object_name = "facilities"

    def get_queryset(self):
        facilities = Facility.objects.filter(deleted=False)
        search_filter = self.request.GET.get("search")
        ward_filter = self.request.GET.get("ward")
        type_filter = self.request.GET.get("type")

        if ward_filter is not None:
            facilities = facilities.filter(ward__name=ward_filter)
        if type_filter is not None:
            facilities = facilities.filter(kind=type_filter)
        if search_filter is not None:
            facilities = facilities.filter(name__icontains=search_filter)
        return facilities

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["wards"] = list(Ward.objects.values_list("name", flat=True))
        return ctx


class GenericFacilityDetailView(AdminAuthMixin, DetailView):
    model = Facility
    template_name = "facilities/detail.html"


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
