from django.shortcuts import render
from .models import Rater,Movie
# Create your views here.

def show_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    avg = movie.average_rating()
    ratings = movie.rating_set.all()

    return render(request,
                'movie_page.html',
                {'movie':movie,
                'ratings':ratings,
                'average':avg})


def top_movies(request):
    movie_list = []
    for movie in Movie.objects.all():
        if type(movie.average_rating()) == float:
            movie_list.append(movie)
    movies = sorted(movie_list, key=lambda x:x.average_rating(),reverse=True)[:20]
    return render(request,
                'movie_listing.html',
                {'movies':movies})

def show_user(request, user_id):
    rater = Rater.objects.get(pk=user_id)
    ratings = rater.rating_set.all()
    return render(request,
                'rater_page.html',
                {'rater':rater,
                'ratings':ratings})
