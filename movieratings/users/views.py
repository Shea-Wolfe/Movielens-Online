from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
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
