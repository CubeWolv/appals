from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # log the user in
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'join/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # create the user
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'join/signup.html', {'form': form})
