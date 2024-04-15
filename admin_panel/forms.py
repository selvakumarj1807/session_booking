from django import forms
from .models import Session, CustomUser

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['subject', 'date', 'time', 'status']  # Fields to include in the form

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'status']  # Fields to include in the form
