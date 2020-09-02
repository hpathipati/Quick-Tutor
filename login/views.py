from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm


def Login(request):
    return HttpResponse("Login Page!")


def Signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user = authenticate(username=username,
                                password=raw_password,
                                first_name=first_name,
                                last_name=last_name)
            login(request, user)
            return redirect('/study')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
