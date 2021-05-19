from django import forms
from .models import Ticket, Review

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        labels = {"title": "Titre"}
        widgets = {"description":forms.Textarea(attrs={"rows":4})}
        
class ReviewForm(forms.ModelForm):
    CHOICES=[("0","0"),
            ("1","1"),
            ("2","2"),
            ("3","3"),
            ("4","4"),
            ("5","5"),
            ]
    rating = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect(), label="Note"
    )
    class Meta :
        model = Review
        fields = ["headline", "rating", "body"]
        labels = {"headline":"Titre", "body":"Commentaire"}       
        widgets = {"body":forms.Textarea(attrs={"rows":4})}

        