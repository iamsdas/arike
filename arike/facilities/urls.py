from django.urls import path

from arike.facilities.views import (
    FacilityCreateView,
    FacilityDeleteView,
    FacilityUpdateView,
    GenericFacilityDetailView,
    GenericFacilityListVeiw,
)

app_name = "facilities"
urlpatterns = [
    path("list/", view=GenericFacilityListVeiw.as_view(), name="list"),
    path("create/", view=FacilityCreateView.as_view(), name="create"),
    path("<pk>/update/", view=FacilityUpdateView.as_view(), name="update"),
    path("<pk>/delete/", view=FacilityDeleteView.as_view(), name="delete"),
    path("<pk>/", view=GenericFacilityDetailView.as_view()),
]
