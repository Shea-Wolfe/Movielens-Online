from django import forms
from django.contrib.auth.models import User
from moviedata.models import Rating, Rater


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')

class RaterForm(forms.ModelForm):
    class Meta:
        model = Rater
        fields = ('gender','age','occupation','zipcode')

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('movie','score','review')

class UserRatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('score','review')
