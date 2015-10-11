from django.shortcuts import render
from .models import Movie, Rater
# Create your views here.

def movie_page(request,movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request,'moviedata/movie_page.html',{'movie':movie})
def rater_page(request,rater_id):
    rater = Rater.objects.get(pk=rater_id)
    return render(request,'moviedata/rater_page.html',{'rater':rater})
