from django.urls import path

from arike.facilities.views import FacilityCreateView

app_name = "facilities"
urlpatterns = [
    path("create/", view=FacilityCreateView.as_view(), name="create"),
]
