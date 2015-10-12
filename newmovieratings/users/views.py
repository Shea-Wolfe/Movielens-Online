from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from moviedata.models import Rater,Rating, Movie
from .forms import LoginForm, RatingForm
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request)
        user = authenticate(username=request.POST['username'],password=request.POST["password"])
        if user is not None and user.is_active:
            login(request,user)
            return redirect('rater_page', rater_id=request.user.rater.pk)
    else:
        form = LoginForm()
        return render(request, 'users/login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

def new_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = user.password
            user.set_password(password)
            user.save()
            rater = Rater(gender='m',age=25,occupation='3',zipcode='60134')
            rater.save()
            user = authenticate(username=user.username,password=password)
            login(request,user)
            return redirect('rater_page', rater_id=rater.pk)


    else:
        form = LoginForm()
    return render(request, 'users/register.html', {'form':form})

def rate_movie(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RatingForm(request.POST)
            if form.is_valid():
                try:
                    rating = Rating.objects.get(movie=request.POST['movie'],
                                                rater=request.user.rater.pk)
                except:
                    rating = Rating(movie=Movie.objects.get(pk=request.POST['movie']),
                                    rater=request.user.rater,
                                    score=request.POST['score'])
                    rating.save()
                    return redirect('rater_page', rater_id=request.user.rater.pk)
                else:
                    rating.score = request.POST['score']
                    rating.save()
                    return redirect('rater_page', rater_id=request.user.rater.pk)
        else:
            form = RatingForm()
        return render(request, 'users/new_rating.html', {'form':form})

def user_rating(request, movie_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRatingForm(request.POST)
            if form.is_valid():
                rating = Rating(movie=Movie.objects.get(pk=movie_id),
                                rater=request.user.rater,
                                score=request.POST['score'])
                rating.save()

        else:
            form = RatingForm()
        return render(request, 'users/unrated.html', {'form':form})
