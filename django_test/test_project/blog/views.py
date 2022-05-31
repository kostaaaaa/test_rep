from django.shortcuts import redirect, render
from django.utils import timezone

from .models import Post
from members.models import UserInfo


def index(request):
    context = Post.objects.order_by('-pub_date')
    context2 = UserInfo.objects.all()
    if request.method == 'POST':
        text = request.POST['text']
        get_image = request.FILES.get('image')
        Post.objects.create(text=text, pub_date=timezone.now(), image=get_image, user_id=request.user.id)
        return redirect('/')

    return render(request, 'index.html', {'context': context, 'context2': context2})
    