from django import forms

from app1.models import Movies

# HTML forms
class Movies_form(forms.Form):
        mtitle = forms.CharField(label='Movie Name', max_length=50)
        hero = forms.CharField(label='Movie Hero', max_length=50)
        heroin = forms.CharField(label='Movie Heroin', max_length=50)
        desc = forms.CharField(label='Description :', max_length=50)
        release_date = forms.DateField(label='Release_date : ')
        mimage = forms.ImageField()

# Model based forms

class MoviesModelform(forms.ModelForm):
        class Meta:
         model=Movies
         fields=['mtitle','hero','heroin','desc','release_date','mimage']


class Employee_form(forms.Form):
    ename=forms.CharField(max_length=30)
    email=forms.CharField(max_length=50)
    esalary=forms.FloatField()
    status=forms.IntegerField()