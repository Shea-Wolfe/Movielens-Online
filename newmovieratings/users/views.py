from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

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
    redirect('top_20')
