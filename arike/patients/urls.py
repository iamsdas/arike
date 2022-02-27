from django.urls import path

from arike.patients.views import (
    PatientCreateView,
    PatientUpdateView,
    PatientListVeiw,
    PatientDetailView,
    FamilyListVeiw,
)

app_name = "patients"
urlpatterns = [
    path("list/", view=PatientListVeiw.as_view(), name="list"),
    path("create/", view=PatientCreateView.as_view(), name="create"),
    path("<pk>/update", view=PatientUpdateView.as_view(), name="update"),
    path("<pk>/family", view=FamilyListVeiw.as_view(), name="family"),
    path("<pk>/", view=PatientDetailView.as_view(), name="details"),
]
