from django.shortcuts import redirect, render
from django.utils import timezone

from .models import Post


def index(request):
    context = Post.objects.order_by('-pub_date')
    if request.method == 'POST':
        text = request.POST['text']
        get_image = request.FILES.get('image')
        Post.objects.create(text=text, pub_date=timezone.now(), image=get_image)
        return redirect('/')

    return render(request, 'index.html', {'context': context})
