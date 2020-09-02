from django import forms
from .models import *


class TutorRequestForm(forms.Form):
    school = forms.ModelChoiceField(queryset=School.objects.all(
    ), widget=forms.Select(attrs={"class": "form-control form-control-sm", "style": "width:25%"}))
    subject = forms.ModelChoiceField(queryset=Subject.objects.none(), widget=forms.Select(
        attrs={"class": "form-control form-control-sm", "style": "width:25%"}))
    course = forms.ModelChoiceField(queryset=Course.objects.none(), widget=forms.Select(
        attrs={"class": "form-control form-control-sm", "style": "width:25%"}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 2}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'course' in self.data:
            try:
                school_id = int(self.data.get('school'))
                self.fields['subject'].queryset = Subject.objects.filter(
                    school_id=school_id).order_by('abbr')
                course_id = int(self.data.get('course'))
                self.fields['course'].queryset = Course.objects.filter(
                    id=course_id).order_by('course_number')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset


class ClaimRequestForm(forms.Form):
    pass
