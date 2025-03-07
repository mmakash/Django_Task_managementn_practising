from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from users.forms import CustomRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from users.forms import LoginForm

# Create your views here.

def sign_up(request):
    form = CustomRegistrationForm()
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print("user", user)
            user.set_password(form.cleaned_data.get('password1')) 
            print(form.cleaned_data)
            user.is_active = False  # Deactivate account till it is confirmed
            user.save()
            messages.success(request, 'Account created successfully. Check your email to activate your account')
            return redirect('sign-in')
        else:
            print("Form is not valid")
    return render(request, 'registration/register.html', {"form": form})


def sign_in(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    return render(request, 'registration/login.html', {"form": form})


def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('sign-in')