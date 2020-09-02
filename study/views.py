from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import TutorRequestForm, ClaimRequestForm
from .models import *
from django.utils import timezone
from django.views import generic


@login_required
def index(request):
    student_requests = tutorRequest.objects.filter(
        student=request.user.student)

    return render(request, 'study/index.html', {'student_requests': student_requests})


@login_required
def tutor_request(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print(request.POST)
        # create a form instance and populate it with data from the request:
        form = TutorRequestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            cour = form.cleaned_data['course']
            desc = form.cleaned_data['description']
            stud = Student.objects.filter(user=request.user)[0]

            newReq = tutorRequest(student=stud, course=cour,
                                  description=desc, pub_date=timezone.now())
            newReq.save()

            return HttpResponseRedirect('/study')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TutorRequestForm()

    return render(request, 'study/request.html', {'form': form})


def load_subjects(request):
    school = request.GET.get('school')
    subjects = Subject.objects.filter(school__abbr=school).order_by('code')
    return render(request, 'study/utils/subjects_dropdown.html', {'subjects': subjects})


def load_courses(request):
    subject = request.GET.get('subject')
    courses = Course.objects.filter(
        subject__code=subject).order_by('course_number')
    return render(request, 'study/utils/courses_dropdown.html', {'courses': courses})


@login_required
def requests_list(request):
    subject = request.GET.get('subject')
    if subject == None:
        unassigned = tutorRequest.objects.filter(
            pub_date__lte=timezone.now()).order_by('-pub_date').exclude(student=request.user.student).filter(tutor=None)[:5]
    else:
        unassigned = tutorRequest.objects.filter(
            course__subject__code=subject).filter(
            pub_date__lte=timezone.now()).order_by('-pub_date').exclude(student=request.user.student).filter(tutor=None)[:5]
    yours = tutorRequest.objects.filter(pub_date__lte=timezone.now()).order_by(
        '-pub_date').filter(tutor=request.user.student)
    return render(request, "study/request_list.html", {"unassigned": unassigned, "yours": yours, 'subject': subject})


def open_request(request, pk):
    if request.method == 'POST':
        form = ClaimRequestForm(request.POST)
        thisReq = tutorRequest.objects.filter(pk=pk)[0]
        thisReq.tutor = request.user.student
        thisReq.save()
    else:
        form = ClaimRequestForm()

    tutor_request = tutorRequest.objects.filter(pk=pk)[0]
    return render(request, "study/open_request.html", {'tutor_request': tutor_request, 'form': form})
