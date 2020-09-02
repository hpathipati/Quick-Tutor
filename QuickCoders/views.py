from django.shortcuts import redirect, render

def homepage(request):
    return render(request, 'study/home.html')