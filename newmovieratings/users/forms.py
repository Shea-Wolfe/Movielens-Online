from django import forms
from django.contrib.auth.models import User
from moviedata.models import Rating

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('movie','score')
