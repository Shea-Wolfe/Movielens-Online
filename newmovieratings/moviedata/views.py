from django.shortcuts import render
from django.db import models

from .models import Movie, Rater, Rating
# Create your views here.

def movie_page(request,movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request,'moviedata/movie_page.html',{'movie':movie})

def rater_page(request,rater_id):
    rater = Rater.objects.get(pk=rater_id)
    return render(request,'moviedata/rater_page.html',{'rater':rater})

def top_20(request):
    top_20 = Movie.objects.annotate(average_rating=models.Avg('rating__score')).order_by('-average_rating')[:20]
    return render(request,'moviedata/top_20.html',{'top_20':top_20})
