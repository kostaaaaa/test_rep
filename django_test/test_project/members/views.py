from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


from blog.models import Post
from .forms import RegisterUserForm
from .models import UserInfo


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome back, {email}!')
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
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, 'Registration complete!')
            return redirect('/')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register-user.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        get_avatar = request.FILES.get('avatar')
        address = request.POST['address']
        UserInfo.objects.create(address=address, avatar=get_avatar, get_user_id=request.user.id)
    
    context2 = UserInfo.objects.filter(get_user=request.user.id)
    context = Post.objects.filter(user=request.user.id).order_by('-pub_date')
    return render(request, 'profile.html', {'context': context, 'context2': context2})


def user_profile(request, username):
    user = User.objects.get(username=username)
    context = Post.objects.filter(user=user).order_by('-pub_date')
    return render(request, 'user_profile.html', {'context': context, 'username': username})
