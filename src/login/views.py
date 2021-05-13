from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def signup(request):
    """Create a user account. """ 
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            messages.success(
                request, 'Votre compte "' + user + '" est bien enregistré'
            )
            return redirect("login:index")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})

def signin(request):
    "Log into a user account."
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request, user)
            return redirect("board:flux")
    else:
        form = AuthenticationForm()
        messages.info(request, "Identifiant ou mot de passe incorrect")
    return render(request, "index.html", {"form": form})


def logOut(request):
    "Disconnect from an user account."
    if request.user.is_authenticated:
        logout(request)
    return redirect("login:index")
