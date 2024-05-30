from django import forms
from .models import Group
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_number', 'email']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'members']