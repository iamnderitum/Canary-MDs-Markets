from django.urls import path
from . import views

app_name = "Profiles"

urlpatterns = [
    path(
        "edit/",
        views.profile_edit,
        name="profile",
    ),
]