from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "board"

urlpatterns = [
    path("flux/", views.display_flux, name="flux"),
    path("posts/", views.display_posts, name="posts"),
    path("review/", views.create_review, name="review"),
    path("comment/", views.add_comment, name="comment"),
    path("delete_review/", views.delete_review, name="delete_review"),
    path("update_review/", views.update_review, name="update_review"),
    path("ticket/", views.create_ticket, name="ticket"),
    path("update_ticket/", views.update_ticket, name="update_ticket"),
    path("delete_ticket/", views.delete_ticket, name="delete_ticket"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)