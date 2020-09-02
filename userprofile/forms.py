
from django import forms
from study.models import Student


class EditProfile(forms.Form):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    email = forms.EmailField()
    graduation_year = forms.ChoiceField(
        choices=[(x, x) for x in range(2020, 2024)])
    picture = forms.URLField(
        required=False, widget=forms.TextInput(attrs={'placeholder': 'Paste URL of picture'}))
    bio = forms.CharField(max_length=200, widget=forms.Textarea(
        attrs={"rows": 5, "cols": 20}), required=False)
