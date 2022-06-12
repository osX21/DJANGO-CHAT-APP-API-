from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib import messages

def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('/')
        else:
            messages.error(request, 'Username or password already exist & Username should not be similar to password. Try again!')
            return redirect('register')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)

def mylogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error('Username or password incorrect. Try again !')
            return redirect('mylogin')

