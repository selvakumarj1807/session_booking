from django import forms
from .models import Session_booking

class SessionBookingForm(forms.ModelForm):
    class Meta:
        model = Session_booking
        fields = ['session', 'username']
