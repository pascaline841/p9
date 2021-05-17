from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import TicketForm, ReviewForm
from .models import Ticket, Review
from follow.models import UserFollows

@login_required
def display_flux(request):
    """Display tickets and review from the following accounts."""
    users = [followed.followed_user for followed in UserFollows.objects.filter(
        user=request.user)]
    users.append(request.user)
    tickets = Ticket.objects.filter(user__in=users).exclude(user=request.user).order_by("-time_created")
    return render(request, "flux.html", {"tickets": tickets})

@login_required
def display_posts(request):
    """Display our tickets or reviews. """
    tickets = Ticket.objects.filter(user=request.user).order_by("-time_created")
    return render(request, "posts.html", {"tickets": tickets})

@login_required
def create_ticket(request):
    """Create ticket to request a review. """
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES["image"] if request.FILES else None
        ticket = Ticket(title=title, description=description,
                        image=image, user=request.user)
        if ticket.is_valid():
            ticket.save()
            return redirect("board:posts")
    else :
        init_values = {}
        if request.user.is_authenticated:
            init_values["user"]= request.user
        form = TicketForm(initial=init_values)
    return render(request, "ticket.html", {"form": form})

@login_required
def delete_ticket(request, ticket_id):
    """Delete a ticket. """
    ticket = Ticket.objects.get(id=ticket_id)
    if request.user == ticket.user:
        ticket.delete()
    return redirect("board:posts")

@login_required
def update_ticket(request, ticket_id):
    """Update a ticket. """
 
@login_required
def create_review(request):
    """Create a ticket and its review in the same time. """
    if request.method != "POST":   
        return render(request, "review.html", {"r": range(6)})
    title = request.POST.get("title")
    description = request.POST.get("description")
    image = request.FILES["image"] if request.FILES else None
    ticket = Ticket(title=title, description=description,
                    image=image, user=request.user)
    if ticket.is_valid():
            ticket.save()
    headline = request.POST.get("headline")
    body = request.POST.get("body")
    rating = request.POST.get("rating")
    review = Review(headline=headline, body=body,
                    rating=rating, ticket=ticket, user=request.user)
    if review.is_valid():
        review.save()
        return redirect("board:posts")

@login_required
def add_comment(request, ticket_id):
    """Add a review to a ticket. """
    if request.method != "POST":   
        return render(request, "comment.html", {"r": range(6)})
    ticket = Ticket.objects.get(id=ticket_id)
    headline = request.POST.get("headline")
    body = request.POST.get("body")
    rating = request.POST.get("rating")
    comment = Review(headline=headline, body=body, rating=rating, ticket=ticket, 
                     user=request.user)
    if comment.is_valid():
        comment.save()
        return redirect("board:posts")

@login_required
def delete_review(request, review_id):
    """Delete a review. """
    review = Review.objects.get(id=review_id)
    if request.user == review.user:
        review.delete()
    return redirect("board:posts")

@login_required
def update_review(request, review_id):
    """Update a review without user ticket. """
    update_review= Review.objects.get(id=review_id)
    if request.method == "GET":
        form = ReviewForm(instance=update_review)
        return render(request, 'comment.html', {"review":update_review, "r":range(6)})
    elif request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance = update_review)    
        if form.is_valid():
            form.save()    
            return redirect("board:posts")
