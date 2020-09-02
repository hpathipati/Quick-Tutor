from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'study'
urlpatterns = [
    path('', views.index, name="index"),
    path('tutor-request/', views.tutor_request, name="tutor_request"),
    path('requests', views.requests_list, name="requests"),
    path('open-request/<int:pk>', views.open_request, name="open_request"),
    path('ajax/load-subjects', views.load_subjects,
         name='ajax_load_subjects'),
    path('ajax/load-courses', views.load_courses,
         name='ajax_load_courses'),
]
