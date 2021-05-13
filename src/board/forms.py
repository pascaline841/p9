from django import forms
from .models import Ticket, Review

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"
        labels = {"title": "Titre"}

    
class ReviewForm(forms.ModelForm):

    class Meta :
        model = Review
        fields = ["ticket", "headline", "rating", "body",]
        labels = {"ticket": "Proposer une critique pour ", 
                  "headline":"Premiere impression", 
                  "rating":"Note", 
                  "body":"Commentaire",
                  }
        RATING=[("0","0"),
            ("1","1"),
            ("2","2"),
            ("3","3"),
            ("4","4"),
            ("5","5"),
            ]
        widgets = {"body":forms.Textarea(attrs={"rows":3}),"rating":forms.ChoiceField(choices=RATING)}


        