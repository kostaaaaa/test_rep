from datetime import datetime
from django.shortcuts import redirect, render

from .models import Message


def index(request):
    info = Message.objects.order_by('-pub_date')
    output = {
        'info': info
    }
    return render(request, 'index.html', output)


def add_message(request):
    info = Message.objects.order_by('-pub_date')
    output = {
        'info': info
    }
    if request.method == 'POST':
        text = request.POST.get("text", False)
        message = Message.objects.create(message_text=text, pub_date=datetime.now())
        return redirect('/blog')
    return render(request, 'add_message.html', output)