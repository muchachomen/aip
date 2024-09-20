from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from .views import home, Ai, register
urlpatterns = [
    path('', home, name='home'),
    path('ai/',  Ai),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'),name= 'login' ),

]
