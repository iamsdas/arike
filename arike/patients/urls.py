from django.urls import path

from arike.patients.views import (
    FamilyListVeiw,
    MemberCreateView,
    MemberUpdateView,
    MemberDeleteView,
    PatientCreateView,
    PatientDetailView,
    PatientListVeiw,
    PatientUpdateView,
)

app_name = "patients"
urlpatterns = [
    path("list/", view=PatientListVeiw.as_view(), name="list"),
    path("create/", view=PatientCreateView.as_view(), name="create"),
    path("<pk>/update/", view=PatientUpdateView.as_view(), name="update"),
    path("<pk>/family/", view=FamilyListVeiw.as_view(), name="family"),
    path("<pk>/family/add/", view=MemberCreateView.as_view(), name="family_add"),
    path("<pk>/family/<id>/", view=MemberUpdateView.as_view(), name="family_update"),
    path("<pk>/family/del/<id>/", view=MemberDeleteView.as_view(), name="family_del"),
    path("<pk>/", view=PatientDetailView.as_view(), name="details"),
]
