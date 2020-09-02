from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import EditProfile
from study.models import Student


@login_required
def index(request):
    return render(request, 'userprofile/index.html')


def index_tutor(request):
    return render(request, 'userprofile/index_tutor.html')


@login_required
def edit_profile(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EditProfile(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            user = request.user
            student = Student.objects.filter(user=user)[0]
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            student.bio = form.cleaned_data['bio']
            student.student_year = form.cleaned_data['graduation_year']
            student.picture = form.cleaned_data['picture']
            student.save()

        return HttpResponseRedirect('/userprofile')

    # if a GET (or any other method) we'll create a blank form
    else:
        student = Student.objects.filter(user=request.user)[0]
        data = {'first_name': student.user.first_name,
                'last_name': student.user.last_name,
                "email": student.user.email,
                "bio": student.bio,
                "graduation_year": student.student_year,
                "picture": student.picture}
        form = EditProfile(data)

        return render(request, 'userprofile/edit.html', {'form': form})
