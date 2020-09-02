from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from .forms import TutorRequestForm


class TutorRequestTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username="harrisonc", password="clark6789")

    def test_number_of_users(self):
        self.assertEqual(User.objects.all().count(), 1)


class StudentRatingsTestCase(TestCase):

    def setUp(self):
        StudentRatings.objects.create(rating=5, comment="helpful")
        StudentRatings.objects.create(rating=1, comment="rude")

    def test_number_of_ratings(self):
        self.assertEquals(StudentRatings.objects.all().count(), 2)

    def test_rating(self):
        five = StudentRatings.objects.get(rating=5)
        self.assertEqual(five.rating, 5)


class CourseTestCase(TestCase):

    def setUp(self):
        School.objects.create(abbr="SEAS", name="E-School")
        Subject.objects.create(
            code="CS", name="Computer Science", school=School.objects.filter(abbr="SEAS")[0])
        Subject.objects.create(
            code="PHYS", name="Physics", school=School.objects.filter(abbr="SEAS")[0])
        Course.objects.create(
            name="Intro to algebra", description="Basic concepts", subject=Subject.objects.filter(code="CS")[0], course_number=101)
        Course.objects.create(
            name="Advanced Physics", description="Complex topics", subject=Subject.objects.filter(code="PHYS")[0], course_number=543)
        Course.objects.create(name="Basic programming", description="for beginners",
                              subject=Subject.objects.filter(code="CS")[0], course_number=110)

    def test_number_courses(self):
        self.assertEquals(Course.objects.all().count(), 3)
        self.assertNotEquals(Course.objects.all().count(), 2)

    def test_check_number(self):
        cs110 = Course.objects.get(name="Basic programming")
        phys543 = Course.objects.get(name="Advanced Physics")
        math101 = Course.objects.get(name="Intro to algebra")
        self.assertEqual(cs110.course_number, "110")
        self.assertEqual(phys543.course_number, "543")
        self.assertNotEqual(math101.course_number, 101)

class test_tutorRequest_form_valid(TestCase):

    def test_tutorForm(self):
        form = TutorRequestForm(data = {
            'school': "SEAS", "subject" : "CS", "course": "CS1010", "description": "help"
        })
        self.assertFalse(form.is_valid())
class test_requestURL(TestCase):
    def test_url_paths(self):
        self.assertEqual(reverse("study:tutor_request"), "/study/tutor-request/")
        self.assertEqual(reverse("study:requests"), "/study/requests")
        self.assertEqual(reverse("study:requests"), "/study/requests")