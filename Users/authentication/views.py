from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .forms import UserAuthForms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def test(request):
    return HttpResponse('Hello World\n This is a test page for my django apllication')


def register(request):
    if request.method == 'POST':
        form = UserAuthForms(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserAuthForms()
    return render(request, 'html/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Connexion réussie.')
            return redirect('dashboard')
        else:
            messages.error(
                request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        form = LoginForm()
    return render(request, 'html/login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, 'Déconnexion réussie.')
    return redirect('login')


def dashboard(request):
    return render(request, 'html/dashboard.html')
