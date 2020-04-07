from django import forms
from django.contrib.auth.models import User
from myfirst_app.models import UserProf

class cv(forms.Form):
    name=forms.CharField(max_length=256)
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)

class User(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')
class User_info_form(forms.ModelForm):
    class Meta():
        model=UserProf
        fields=('portfolio','profile_pic')
