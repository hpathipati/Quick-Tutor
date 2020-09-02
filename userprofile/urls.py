from django.contrib import admin
from django.urls import path,include

from . import views

app_name = 'userprofile'
urlpatterns = [
    path('', views.index, name="index"),
    path('index_tutor/', views.index_tutor, name="index_tutor"),
    path('edit/', views.edit_profile, name="edit")
]
