from django.shortcuts import render
from .models import Rater,Movie
# Create your views here.

def show_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    avg = movie.average_rating()
    ratings = movie.ratings_set.all()

    return render(request,
                'movie_page.html',
                {'movie':movie,
                'ratings':ratings,
                'average': avg})


def top_movies(request):
    movies = Movie.objects.orderby('-average_rating()')[:20]
    top_20 = [str(movie) for movie in movies]
    return render(request,
                'movies.html',
                {'movies':top_20})

def show_user(request, user_id):
    rater = Rater.objects.get(pk=user_id)
    ratings = rater.rating_set.all()
    return render(request,
                'rater_page.html',
                {'rater':rater,
                'ratings':ratings})
