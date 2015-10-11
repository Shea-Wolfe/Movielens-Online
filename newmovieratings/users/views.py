from django.shortcuts import render
from django.contrib.auth import authenticate

from .forms import LoginForm
# Create your views here.
def login(request):
    if request.method == 'POST':
        pass
    else:
        form = LoginForm()
        return render(request, 'users/login.html', {'form':form})

def logout(request):
    logout(request)
    redirect('top_20')
