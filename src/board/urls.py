from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "board"

urlpatterns = [
    path("flux/", views.display_flux, name="flux"),
    path("posts/", views.display_posts, name="posts"),
    path("review/", views.create_review, name="review"),
    path("comment/<str:ticket_id>", views.add_comment, name="comment"),
    path("delete_review/<str:review_id>", views.delete_review, name="delete_review"),
    path("update_review/<str:review_id>", views.update_review, name="update_review"),
    path("ticket/", views.create_ticket, name="ticket"),
    path("update_ticket/<str:ticket_id>", views.update_ticket, name="update_ticket"),
    path("delete_ticket/<str:ticket_id>", views.delete_ticket, name="delete_ticket"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)