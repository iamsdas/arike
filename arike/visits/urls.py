from django.urls import path

from arike.visits.views import (
    ScheduleCreateView,
    ScheduleDeleteView,
    ScheduleDetailView,
    ScheduleListVeiw,
    ScheduleUpdateView,
    TreatmentNoteCreateView,
    TreatmentsListVeiw,
    VisitDetailsCreateView,
)

app_name = "visits"
urlpatterns = [
    path("schedule/", view=ScheduleListVeiw.as_view(), name="list"),
    path("create/", view=ScheduleCreateView.as_view(), name="create"),
    path("<pk>/visit/", view=VisitDetailsCreateView.as_view(), name="visit"),
    path("<pk>/", view=ScheduleDetailView.as_view(), name="view"),
    path("<pk>/update/", view=ScheduleUpdateView.as_view(), name="update"),
    path("<pk>/delete/", view=ScheduleDeleteView.as_view(), name="delete"),
    path("<pk>/treatments/", view=TreatmentsListVeiw.as_view(), name="treatments"),
    path(
        "<pk>/treatments/<id>/addnote",
        view=TreatmentNoteCreateView.as_view(),
        name="add_note",
    ),
]
