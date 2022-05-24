from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from blog.models import Post
from .forms import RegisterUserForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('/')
        else:
            messages.error(request, 'Error logging in.. Please, try again!')
            return redirect('/members/login-user')  
    
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.warning(request, 'You were log out!')
    return redirect('/')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration complete!')
            return redirect('/')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register-user.html', {'form':form})


def profile(request):
    context = Post.objects.filter(username=request.user.get_username()).order_by('-pub_date')
    return render(request, 'profile.html', {'context':context})


def user_profile(request, username):
    context = Post.objects.filter(username=username).order_by('-pub_date')
    return render(request, 'user-profile.html', {'context': context, 'username': username})
