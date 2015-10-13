from django.shortcuts import render
from django.db import models
from .models import Rater,Movie
# Create your views here.

def show_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.user.is_authenticated():
        for rating in request.user.rater.rating_set.all():
            if rating.movie == movie:
                return render(request,
                            'movie_data/movie_page.html',
                            {'movie':movie})
        return render(request,
                    'movie_data/rate_movie_page.html',
                    {'movie':movie})

    else:
        return render(request,
                'movie_data/movie_page.html',
                {'movie':movie})


def top_movies(request):
    movie_list = []
    # for movie in Movie.objects.all():
    #     if type(movie.average_rating()) == float:
    #         movie_list.append(movie)
    # movies = sorted(movie_list, key=lambda x:x.average_rating(),reverse=True)[:20]
    filtered = Movie.objects.annotate(num_ratings=models.Count('rating')).filter(num_ratings__gte=50)
    movies = filtered.annotate(models.Avg('rating__score')).order_by('-rating__score__avg')[:20]
    return render(request,
                'movie_data/movie_listing.html',
                {'movies':movies})

def show_user(request, user_id):
    rater = Rater.objects.get(pk=user_id)
    return render(request,
                'movie_data/rater_page.html',
                {'rater':rater})
