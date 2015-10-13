from django.shortcuts import render
from django.db import models
from django.contrib.auth import authenticate

from .models import Movie, Rater, Rating
# Create your views here.

def movie_page(request,movie_id):
    movie = Movie.objects.get(pk=movie_id)
    ratings = Rating.objects.filter(movie=movie)
    ratings = ratings.select_related('rater')
    if request.user.is_authenticated():
        try:
            Rating.objects.get(movie=movie.pk, rater=request.user.rater.pk)
        except:
            return render(request,'users/unrated.html',{'movie':movie,
                                                        'ratings':ratings})
        else:
            return render(request,'moviedata/movie_page.html',{'movie':movie,
                                                                'ratings':ratings})
    else:
        return render(request,'moviedata/movie_page.html',{'movie':movie,
                                                            'ratings':ratings})

def rater_page(request,rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings = Rating.objects.filter(rater=rater)
    ratings = ratings.select_related('movie')
    if request.user.is_authenticated():
        return render(request, 'moviedata/user_movie_page.html',{'rater':rater,
                                                                'ratings':ratings})
    return render(request,'moviedata/rater_page.html',{'rater':rater,
                                                        'ratings':ratings})

def top_20(request):
    pop_movies = Movie.objects.annotate(num_ratings=models.Count('rating')).filter(num_ratings__gte=50)
    top_20 = pop_movies.annotate(average_rating=models.Avg('rating__score')).order_by('-average_rating')[:20]
    return render(request,'moviedata/top_20.html',{'top_20':top_20})

def top_20_rated(request):
    top_20 = Movie.objects.annotate(total_ratings=models.Count('rating')).order_by('-total_ratings')[:20]
    return render(request,'moviedata/top_20.html',{'top_20':top_20})

def review_page(request, movie_id, rater_id):
    movie = Movie.objects.get(pk=movie_id)
    rater = Rater.objects.get(pk=rater_id)
    rating = Rating.objects.get(movie=movie,rater=rater)
    return render(request,'moviedata/review_page.html',{'rating':rating,
                                                        'movie':movie,
                                                        'rater':rater})
