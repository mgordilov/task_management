from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from tm_app.models import Task
from . import models
from . import forms
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def profile(request):
    tasks = Task.objects.filter(assigned_to=request.user) | Task.objects.filter(managed_by=request.user)
    return render(request, 'users/profile.html', {'tasks': tasks})

def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                return redirect(next_url or 'home')
    else:
        form = forms.LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'users/logout.html')

def register(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = forms.UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile_update(request, pk):
    if request.method == 'POST':
        user_form = forms.UserUpdateForm(request.POST, instance=request.user)
        profile_form = forms.UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = forms.UserUpdateForm(instance=request.user)
        profile_form = forms.UserProfileUpdateForm(instance=request.user.userprofile)
    return render(request, 'users/profile_update.html', {'user_form': user_form, 'profile_form': profile_form})