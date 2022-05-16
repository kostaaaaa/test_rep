from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_message', views.add_message, name='add_message')
]