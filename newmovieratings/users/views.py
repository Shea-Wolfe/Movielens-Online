from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from datetime import datetime
from moviedata.models import Rater,Rating, Movie
from .forms import LoginForm, RatingForm, UserRatingForm
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
            return render(request, 'users/login.html', {'form':form,'failed':True})
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
            rater = Rater(gender='m',age=25,occupation='3',zipcode='60134',user=user)
            rater.save()
            user = authenticate(username=user.username,password=password)
            login(request,user)
            return redirect('rater_page', rater_id=rater.pk)


    else:
        form = LoginForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def rate_movie(request):
        if request.method == 'POST':
            form = RatingForm(request.POST)
            if form.is_valid():
                try:
                    rating = Rating.objects.get(movie=request.POST['movie'],
                                                rater=request.user.rater.pk)
                except:
                    rating = form.save(commit=False)
                    rating.rater = request.user.rater
                    rating.timestamp = datetime.now()
                    rating.save()
                    messages.add_message(request, messages.SUCCESS, "Rating Created!")
                    return redirect('rater_page', rater_id=request.user.rater.pk)
                else:
                    rating.score = request.POST['score']
                    rating.timestamp = datetime.now()
                    rating.save()
                    messages.add_message(request, messages.SUCCESS, "Rating Edited!")
                    return redirect('rater_page', rater_id=request.user.rater.pk)
        else:
            form = RatingForm()
        return render(request, 'users/new_rating.html', {'form':form})

@login_required
def user_rating(request, movie_id):
    if request.method == 'POST':
        form = UserRatingForm(request.POST)
        if form.is_valid():
            try:
                rating = Rating.objects.get(movie=Movie.objects.get(pk=movie_id),rater=request.user.rater)
            except:
                rating = form.save(commit=False)
                rating.rater = request.user.rater
                rating.movie = Movie.objects.get(pk=movie_id)
                rating.timestamp = datetime.now()
                rating.save()
                messages.add_message(request, messages.SUCCESS, "Rating Created!")
                return redirect('rater_page',rater_id=request.user.rater.pk)
            else:
                rating.score = request.POST['score']
                rating.review = request.POST['review']
                rating.timestamp = datetime.now()
                rating.save()
                messages.add_message(request, messages.SUCCESS, "Rating Edited!")
                return redirect('rater_page',rater_id=request.user.rater.pk)

    else:
        form = UserRatingForm()
    return render(request, 'users/user_rating.html', {'form':form,
                                                    'movie':movie_id})

@login_required
def remove_rating(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.rating_set.filter(rater=request.user.rater).delete()
    messages.add_message(request, messages.SUCCESS, "Rating Deleted!")
    return redirect('rater_page',rater_id=request.user.rater.pk)
