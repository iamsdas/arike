from re import template
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from arike.facilities.models import Ward
from arike.visits.forms import VisitDetailsForm, VisitScheduleForm
from arike.visits.models import VisitDetails, VisitSchedule


class GenericScheduleFormView(LoginRequiredMixin):
    form_class = VisitScheduleForm
    template_name = "schedule/form.html"

    def get_queryset(self):
        return VisitSchedule.objects.filter(nurse=self.request.user, deleted=False)

    def get_success_url(self):
        return reverse_lazy("visits:list")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.nurse = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ScheduleCreateView(GenericScheduleFormView, CreateView):
    pass


class ScheduleUpdateView(GenericScheduleFormView, UpdateView):
    pass


class ScheduleDeleteView(GenericScheduleFormView, DeleteView):
    def delete(self, request, *args: str, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.deleted = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class ScheduleDetailView(LoginRequiredMixin, DetailView):
    model = VisitSchedule
    template_name = "schedule/detail.html"


class ScheduleListVeiw(LoginRequiredMixin, ListView):
    model = VisitSchedule
    template_name = "schedule/list.html"
    context_object_name = "visits"

    def get_queryset(self):
        return (
            VisitSchedule.objects.filter(
                nurse=self.request.user, date__gte=datetime.now().date(), deleted=False
            )
            .order_by("date")
            .order_by("time")
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["wards"] = list(Ward.objects.values_list("name", flat=True))
        return ctx


class GenericVisitDetailsFormView(LoginRequiredMixin):
    form_class = VisitDetailsForm
    template_name = "schedule/form.html"

    def get_queryset(self):
        return VisitDetails.objects.filter(deleted=False)

    def get_success_url(self):
        return reverse_lazy("visits:view", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.schedule = VisitSchedule.objects.get(pk=self.kwargs["pk"])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class VisitDetailsCreateView(GenericVisitDetailsFormView, CreateView):
    pass
