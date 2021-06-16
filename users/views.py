from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import login, logout, authenticate
from users.forms import UserRegistration, UserAuthentication
from users.models import User
from django.contrib import messages
import requests
import os

# Create your views here.

def home_view(request,  *args, **kwargs):
    context = {
        'use': User.objects.all()
    }
    return render(request, 'users/home.html', context)

def login_view(request):
    
    user = request.user
    if user.is_authenticated: 
        return redirect("users-home")

    if request.POST:
        form = UserAuthentication(request.POST)
        if form.is_valid():
            email=request.POST.get('email')
            password=request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user:
                login(request,user)
                return redirect('users-home')
    else:
        form = UserAuthentication()
    return render(request,'users/login.html',{'form':form,})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            address = form.cleaned_data.get('address')
            users = authenticate(username=username, email=email, password=password, confirm_password=confirm_password, address=address)
            login(request, users)
            form = UserRegistration()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('users-home')
    else:
        form = UserRegistration()
    use = User.objects.all()
    return render(request, 'users/register.html', {'form': form, 'us': use})

def logout_view(request):
    logout(request)
    return redirect('/')

def edit_view(request, id):
    if request.method == 'POST':
      pi = User.objects.get(pk=id)
      form = UserRegistration(request.POST, instance=pi)
      if form.is_valid():
        form.save()
        return HttpResponseRedirect('/', {'form' : form})
    else:
      pi = User.objects.get(pk=id)
      form = UserRegistration(instance=pi)
    return render(request, 'users/edit.html', {'form' : form})


def delete_view(request, id):
    if request.method == 'POST':
      pi = User.objects.get(pk=id)
      pi.delete()
      return HttpResponseRedirect('/')  
