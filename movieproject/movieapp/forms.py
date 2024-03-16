from django import forms
from .models import Movie, Review, Rating


class MovieForm (forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','slug','desc','release','img','actors','category','trailer_link']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating_value']