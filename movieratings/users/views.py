from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import UserForm, RaterForm
from movie_data.models import Rater

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        # attempting to log in
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('user_page',user_id=user.rater.pk)
        else:
            return render(request,
                          'users/login.html',
                          {'failed': True,
                           'username': username})

    return render(request,
                  'users/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')

def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            password = user.password

            user.set_password(password)
            user.save()

            rater = Rater(
                user=user,
                gender='m',
                age='25',
                occupation='1'
            )
            rater.save()

            user = authenticate(username=user.username,
                                password=password)
            login(request, user)
            return redirect('user_page',user_id=rater.pk)
    else:
        form = UserForm()
    return render(request, 'users/register.html',
                  {'form': form})
