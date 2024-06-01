from django import forms
from .models import Group,Contact,MarketingPorCorreoPersonal


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_number', 'email']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'members']

class MarketingPorCorreoPersonalForm(forms.ModelForm):
    class Meta:
        model = MarketingPorCorreoPersonal
        fields = ['cuerpoDelCorreo', 'tipoCorreo', 'emailDeDestino']

    emailDeDestino = forms.ModelChoiceField(
        queryset=Contact.objects.all(),
        label="Contacto de Destino",
        widget=forms.Select
    )