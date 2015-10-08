from django.shortcuts import render
from django.http import HttpResponse
from .models import Rating,User,Movie
# Create your views here.

def show_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    avg = movie.average_rating()
    ratings = movie.ratings_set.all()

    return render(request,
                'movie_page.html',
                {'movie':movie,
                'ratings':ratings
                'average': avg})


def top_movies(request):
    Movies = Movie.objects.orderby('-average_rating()')[:20]
    top_20 = [string(movie) for movie in Movies]
    return render(request,
                'movies.html',
                {'movies':top_20})

def show_user(request, user_id):
    rater = Rater.objects.get(pk=user_id)
    ratings = rater.ratings_set.all()
    return render(request,
                'rater_page.html'
                {'rater':rater,
                'ratings':ratings})
