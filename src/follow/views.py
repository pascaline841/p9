from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect

from .models import UserFollows

@login_required
def followup(request):
    """Add users to subscription function."""
    context = {"user_follows": UserFollows.objects.all()}
    if request.method == "POST":
        username_to_follow = request.POST.get("username")   
        try:
            new_followed = User.objects.get(username=username_to_follow)
        except User.DoesNotExist:
            messages.info(request, "Utilisateur inconnu !")
        else:
            if new_followed == request.user:
                messages.info(request, "Impossible !")
            else:
                try:
                    followed = UserFollows(user=request.user,
                                     followed_user=new_followed)
                    followed.save()
                except IntegrityError:
                    messages.info(request, "Vous etes déjà abonnés à cet utilisateur !")
    return render(request, "follow.html", context)


@login_required
def unfollow(request, user_to_unfollow):
    """Unsubscribe users function. """
    user_to_unfollow = User.objects.get(username=user_to_unfollow)
    for followed in UserFollows.objects.all():
        if (followed.user, followed.followed_user) == (request.user, user_to_unfollow):
            followed.delete()
    return redirect("follow:follow")
