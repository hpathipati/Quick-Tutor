from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'login'
urlpatterns = [
    # path('', views.Login, name="index"),
    path('', include('django.contrib.auth.urls'), name="login"),
    path('signup/', views.Signup, name='signup'),
]
