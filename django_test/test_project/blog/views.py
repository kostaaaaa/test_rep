from contextlib import nullcontext
from email.mime import image
from django.shortcuts import redirect, render
from django.utils import timezone

from .models import Post


def index(request):
    content = Post.objects.order_by('-pub_date')

    return render(request, 'index.html', {'content': content})


def new_post(request):
    content = Post.objects.order_by('-pub_date')
    if request.method == 'POST':
        text = request.POST['text']
        get_image = request.FILES['image']
        Post.objects.create(text=text, pub_date=timezone.now(), image=get_image)
        return redirect('/')

    return render(request, 'new-post.html', {'content': content})
