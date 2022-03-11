from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    RedirectView,
    UpdateView,
)

from arike.facilities.models import Facility
from arike.users.forms import UserForm, UserSignupForm
from arike.users.models import UserRoles

User = get_user_model()


class AdminAuthMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == UserRoles.DISTRICT_ADMIN


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserFormView(AdminAuthMixin):
    form_class = UserForm
    template_name = "users/user_form.html"
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_queryset(self):
        district = self.request.user.facility.ward.lsg_body.district
        users = User.objects.filter(
            deleted=False, facility__ward__lsg_body__district=district
        ).exclude(role=UserRoles.DISTRICT_ADMIN)
        return users

    def get_success_url(self):
        return "/"


class NurseSignUpView(UserFormView, CreateView):
    form_class = UserSignupForm
    pass


class NurseDeleteView(UserFormView, DeleteView):
    def delete(self, request: HttpRequest, *args: str, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.deleted = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class NurseUpdateView(UserFormView, UpdateView):
    pass


class UserListVeiw(AdminAuthMixin, ListView):
    model = User
    template_name = "users/list.html"
    context_object_name = "users"

    def get_queryset(self):
        district = self.request.user.facility.ward.lsg_body.district
        users = User.objects.filter(
            deleted=False, facility__ward__lsg_body__district=district
        ).exclude(role=UserRoles.DISTRICT_ADMIN)
        search_filter = self.request.GET.get("search")
        role_filter = self.request.GET.get("role")
        facility_filter = self.request.GET.get("facility")

        if search_filter is not None:
            users = users.filter(name__icontains=search_filter)
        if role_filter is not None:
            users = users.filter(role=role_filter)
        if facility_filter is not None:
            users = users.filter(facility=facility_filter)
        return users

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        district = self.request.user.facility.ward.lsg_body.district
        ctx["facilities"] = Facility.objects.filter(ward__lsg_body__district=district)

        return ctx


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["name", "email", "phone", "facility"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
