from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import NewUserForm
from .models import Post


def index(request):
    context = Post.objects.order_by('-pub_date')
    if request.method == 'POST':
        text = request.POST['text']
        get_image = request.FILES.get('image')
        get_user = request.user.get_username()
        Post.objects.create(text=text, pub_date=timezone.now(), image=get_image, username=get_user)
        return redirect('/')

    return render(request, 'index.html', {'context': context})
    