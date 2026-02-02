from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hjem/", views.home, name="home"),
    path("projekter/", views.projekter, name="projekter"),
    path("kontakt/", views.kontakt, name="kontakt"),
    path("omOs/", views.omOs, name="omOs"),
]
