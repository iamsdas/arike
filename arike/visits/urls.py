from django.urls import path

from arike.visits.views import (
    ScheduleCreateView,
    ScheduleUpdateView,
    ScheduleDeleteView,
    ScheduleListVeiw,
    ScheduleDetailView,
)

app_name = "visits"
urlpatterns = [
    path("schedule/", view=ScheduleListVeiw.as_view(), name="list"),
    path("create/", view=ScheduleCreateView.as_view(), name="create"),
    path("<pk>/", view=ScheduleDetailView.as_view(), name="view"),
    path("<pk>/update/", view=ScheduleUpdateView.as_view(), name="update"),
    path("<pk>/delete/", view=ScheduleDeleteView.as_view(), name="delete"),
]
