from django.urls import path

from . import views

app_name = "follow"


urlpatterns = [
    path("", views.followup, name="follow"),
    path("unfollow/<user_to_unfollow>", views.unfollow, name="unfollow"),
]
