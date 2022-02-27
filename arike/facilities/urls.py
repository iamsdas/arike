from django.urls import path

from arike.facilities.views import (
    FacilityCreateView,
    GenericFacilityListVeiw,
    GenericFacilityDetailView,
)

app_name = "facilities"
urlpatterns = [
    path("list/", view=GenericFacilityListVeiw.as_view(), name="list"),
    path("create/", view=FacilityCreateView.as_view(), name="create"),
    path("<pk>/", view=GenericFacilityDetailView.as_view()),
]
