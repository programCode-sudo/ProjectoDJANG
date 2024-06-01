from django import forms
from .models import Group,Contact,MarketingPorCorreoPersonal, CampañaDeMarketing


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_number', 'email']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'members']

class MarketingPorCorreoPersonalForm(forms.ModelForm):
    TIPO_CORREO_CHOICES = [
        ('Promocional', 'Promocional'),
        ('Informativo', 'Informativo'),
        ('Urgente', 'Urgente'),
    ]

    tipoCorreo = forms.ChoiceField(
        choices=TIPO_CORREO_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = MarketingPorCorreoPersonal
        fields = ['cuerpoDelCorreo', 'tipoCorreo', 'emailDeDestino']

    emailDeDestino = forms.ModelChoiceField(
        queryset=Contact.objects.all(),
        label="Contacto de Destino",
        widget=forms.Select
    )
class CampañaDeMarketingForm(forms.ModelForm):
    TIPO_CORREO_CHOICES = [
        ('Promocional', 'Promocional'),
        ('Informativo', 'Informativo'),
        ('Urgente', 'Urgente'),
    ]

    tipoCorreo = forms.ChoiceField(
        choices=TIPO_CORREO_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = CampañaDeMarketing
        fields = ['nombre', 'tipoCorreo', 'cuerpoDelCorreo', 'grupo']