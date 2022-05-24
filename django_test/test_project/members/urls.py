from django.urls import path

from . import views


urlpatterns = [
    path('login-user', views.login_user, name='login'),
    path('logout-user', views.logout_user, name='logut'),
    path('register-user', views.register_user, name='register'),
    path('profile', views.profile, name='profile'),
    path("<str:username>/", views.user_profile, name = "user_profile"),
]
