from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DetailView, RedirectView, UpdateView

from arike.users.forms import UserSignupForm
from arike.users.models import UserRoles, User as UserModel

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class AdminAuthMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == UserRoles.DISTRICT_ADMIN


class UserFormView(AdminAuthMixin):
    form_class = UserSignupForm
    template_name = "users/user_form.html"

    def get_queryset(self):
        return UserModel.objects.all()

    def get_success_url(self):
        return "/"


class NurseSignUpView(UserFormView, CreateView):
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

        if search_filter is not None:
            users = users.filter(name__icontains=search_filter)
        return users


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
