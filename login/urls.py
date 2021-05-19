
from django.urls import path
from . import views


app_name = "login"

urlpatterns = [
    path("", views.signin, name="index"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logOut, name="logout"),
]