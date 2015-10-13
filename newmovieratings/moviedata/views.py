from django.shortcuts import render
from django.db import models
from django.contrib.auth import authenticate

from .models import Movie, Rater, Rating
# Create your views here.

def movie_page(request,movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.user.is_authenticated():
        try:
            Rating.objects.get(movie=movie.pk, rater=request.user.rater.pk)
        except:
            return render(request,'users/unrated.html',{'movie':movie})
        else:
            return render(request,'moviedata/movie_page.html',{'movie':movie})
    else:
        return render(request,'moviedata/movie_page.html',{'movie':movie})

def rater_page(request,rater_id):
    rater = Rater.objects.get(pk=rater_id)
    if request.user.is_authenticated():
        return render(request, 'moviedata/user_movie_page.html',{'rater':rater})
    return render(request,'moviedata/rater_page.html',{'rater':rater})

def top_20(request):
    top_20 = Movie.objects.annotate(average_rating=models.Avg('rating__score')).order_by('-average_rating')[:20]
    return render(request,'moviedata/top_20.html',{'top_20':top_20})

def top_20_rated(request):
    top_20 = Movie.objects.annotate(total_ratings=models.Count('rating')).order_by('-total_ratings')[:20]
    return render(request,'moviedata/top_20.html',{'top_20':top_20})
