from django import forms
from django.forms import ModelForm
from .models import Event

# create a venue form

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'mobile_no', 'email_address')
        labels = {
            'name': 'Enter Your Name Here',
            'event_date': 'Enter Date YYYY/MM/DD',
            'venue': 'Ticket no.',
            'mobile_no': 'Enter Your Mobile Number',
            'email_address': 'Put Here Email Address',            
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name'}),
            'event_date': forms.DateTimeInput(attrs={'class':'form-control', 'placeholder': 'Date'}),
            'venue': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ticket no'}),
            'mobile_no': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Mobile Number'}),
            'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}),
        }
