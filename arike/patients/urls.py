from django.urls import path

from arike.patients.views import (
    DiseaseCreateView,
    DiseaseDeleteView,
    DiseaseListVeiw,
    DiseaseUpdateView,
    FamilyListVeiw,
    MemberCreateView,
    MemberDeleteView,
    MemberUpdateView,
    PatientCreateView,
    PatientDetailView,
    PatientListVeiw,
    PatientUpdateView,
    TreatmentCreateView,
    TreatmentDeleteView,
    TreatmentsListVeiw,
    TreatmentUpdateView,
    VisitDetailsDetailView,
    VisitListVeiw,
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
    path("<pk>/disease/", view=DiseaseListVeiw.as_view(), name="disease"),
    path("<pk>/disease/add/", view=DiseaseCreateView.as_view(), name="disease_add"),
    path(
        "<pk>/disease/update/<id>/",
        view=DiseaseUpdateView.as_view(),
        name="disease_update",
    ),
    path("<pk>/disease/del/<id>/", view=DiseaseDeleteView.as_view(), name="dis_del"),
    path("<pk>/treatment/", view=TreatmentsListVeiw.as_view(), name="treatments"),
    path("<pk>/treatment/add/", view=TreatmentCreateView.as_view(), name="trtmnt_add"),
    path(
        "<pk>/treatment/update/<id>/",
        view=TreatmentUpdateView.as_view(),
        name="trtmnt_update",
    ),
    path(
        "<pk>/treatment/del/<id>/",
        view=TreatmentDeleteView.as_view(),
        name="trtmnt_del",
    ),
    path("<pk>/", view=PatientDetailView.as_view(), name="details"),
    path("<pk>/history/", view=VisitListVeiw.as_view(), name="visits"),
    path(
        "<pk>/history/<id>/",
        view=VisitDetailsDetailView.as_view(),
        name="visit_details",
    ),
]
