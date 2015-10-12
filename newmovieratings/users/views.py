from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from moviedata.models import Rater
from .forms import LoginForm
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request)
        user = authenticate(username=request.POST['username'],password=request.POST["password"])
        if user is not None and user.is_active:
            login(request,user)
            return redirect('top_20')
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
