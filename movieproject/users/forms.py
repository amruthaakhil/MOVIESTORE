from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(AuthenticationForm):
    username=forms.CharField(max_length=250,required=True,widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control',}))
    password = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control','data-toggle':'password','id':'password','name':'password'}))

    class Meta:
        model=User
        fields=['username','password']

class UpdateProfileForm(forms.ModelForm):
    bio=forms.CharField(max_length=250,required=True,widget=forms.TextInput(attrs={'class':'form-control',}))

    class Meta:
        model=Profile
        fields=['bio']
        labels = {
            'bio': 'Bio'
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40})  # Customize textarea attributes as needed
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']