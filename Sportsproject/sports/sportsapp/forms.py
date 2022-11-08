from django import forms
from sportsapp.models import Sports
class SportsForms(forms.ModelForm):
    class Meta:
        model=Sports
        fields=['name','img','desc','country']