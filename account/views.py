from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from blognews.views import blognews
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import authenticate, login as dj_login


def login(request):
    page = 'login'

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        

        user = authenticate(request, username=username, password=password)

        if user is not None:
            dj_login(request, user)
            return redirect('blognews')

        else:
            messages.info(request, 'Invalid username or password')
            return redirect("login")
    if 'next' in request.POST:
        return redirect(request.POST['next'])

    return render(request, 'join/login.html', {'page': page})



def logoutUser(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            #login(request, user)
            return redirect('blognews')
    else:
        form = SignupForm()
    return render(request, 'join/signup.html', {'form': form})
