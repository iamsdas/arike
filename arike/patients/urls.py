from django.urls import path

from arike.patients.views import (
    PatientCreateView,
    PatientUpdateView,
    GenericPatientListVeiw,
    GenericPatientDetailView,
)

app_name = "patients"
urlpatterns = [
    path("list/", view=GenericPatientListVeiw.as_view(), name="list"),
    path("create/", view=PatientCreateView.as_view(), name="create"),
    path("<pk>/update", view=PatientUpdateView.as_view(), name="update"),
    path("<pk>/", view=GenericPatientDetailView.as_view(), name="details"),
]
