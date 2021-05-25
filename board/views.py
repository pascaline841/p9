from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import TicketForm, ReviewForm
from .models import Ticket, Review
from follow.models import UserFollows


@login_required
def display_flux(request):
    """Display tickets and reviews from the following accounts."""
    users = [
        followed.followed_user
        for followed in UserFollows.objects.filter(user=request.user)
    ]
    users.append(request.user)
    tickets = Ticket.objects.filter(user__in=users).order_by("-time_created")
    return render(request, "flux.html", {"tickets": tickets})


@login_required
def display_posts(request):
    """Display our tickets or reviews."""
    tickets = Ticket.objects.filter(user=request.user).order_by("-time_created")
    return render(request, "posts.html", {"tickets": tickets})


@login_required
def create_ticket(request):
    """Create ticket to request a review."""
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.image = request.FILES
            ticket.user = request.user
            ticket.save()
            return redirect("board:posts")
    else:
        form = TicketForm()
    context = {"form": form}
    return render(request, "ticket.html", context)


@login_required
def delete_ticket(request, ticket_id):
    """Delete a ticket."""
    ticket = Ticket.objects.get(id=ticket_id)
    if request.user == ticket.user:
        ticket.delete()
    return redirect("board:posts")


@login_required
def update_ticket(request, ticket_id):
    """Update a ticket."""
    instance_ticket = Ticket.objects.get(id=ticket_id)

    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=instance_ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("board:posts")
    else:
        form = TicketForm(instance=instance_ticket)
    context = {"form": form}
    return render(request, "ticket.html", context)


@login_required
def create_review(request):
    """Create a ticket and its review in the same time."""
    if request.method == "POST":
        form_ticket = TicketForm(request.POST, request.FILES)
        if form_ticket.is_valid():
            ticket = form_ticket.save(commit=False)
            ticket.user = request.user
            ticket.save()
            form_review = ReviewForm(request.POST)
            if form_review.is_valid():
                review = form_review.save(commit=False)
                review.ticket = ticket
                review.user = request.user
                review.save()
            return redirect("board:posts")
    else:
        form_ticket = TicketForm()
        form_review = ReviewForm()
    context = {"form_ticket": form_ticket, "form_review": form_review}
    return render(request, "review.html", context)


@login_required
def add_comment(request, ticket_id):
    """Add a review to a ticket."""
    instance_ticket = Ticket.objects.get(id=ticket_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.ticket = instance_ticket
            comment.save()
            return redirect("board:flux")
    else:
        form = ReviewForm()
    context = {"form": form, "ticket": instance_ticket}
    return render(request, "comment.html", context)


@login_required
def delete_review(request, review_id):
    """Delete a review."""
    review = Review.objects.get(id=review_id)
    if request.user == review.user:
        review.delete()
    return redirect("board:posts")


@login_required
def update_review(request, review_id):
    """Update a review."""
    instance_review = Review.objects.get(id=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=instance_review)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect("board:flux")
    else:
        form = ReviewForm(instance=instance_review)
    context = {"form": form}
    return render(request, "comment.html", context)
