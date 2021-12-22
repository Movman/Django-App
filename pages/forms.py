from django import forms
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def create_contact(self, **validated_data):
        Contact.objects.create(
            name = validated_data.get('name'),
            email = validated_data.get('email'),
            message = validated_data.get('message')
        )