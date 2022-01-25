from django import forms
from django.forms import TextInput, EmailInput
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'message': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Message'
            })
        }