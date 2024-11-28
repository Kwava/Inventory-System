from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class CreateUserForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','password1','password2']

       
class UpdateUserForm(forms.ModelForm):
    
    class Meta:
        model=User
        fields=['username','email']


class UpdateProfileForm(forms.ModelForm):
    
    class Meta:
        model=Profile
        fields=['adress','phone','image']
        
       