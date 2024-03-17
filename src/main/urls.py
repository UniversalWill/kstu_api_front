from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notes/", include("notes.urls")),
    path("journal/", include("journal.urls")),
    path("schedule/", include("schedule.urls")),
    path("login/", include("login.urls")),
]
