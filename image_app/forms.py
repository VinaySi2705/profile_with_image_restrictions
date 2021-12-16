from django import forms
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','profile_photo','email','mobile_no']
