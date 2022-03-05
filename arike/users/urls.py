from django.urls import path

from arike.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    NurseSignUpView,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("register/", view=NurseSignUpView.as_view(), name="create"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
