from django import forms
from .models import Evento, Group,Contact,MarketingPorCorreoPersonal, CampañaDeMarketing, Sms


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

class EventoForm(forms.ModelForm):
    fecha_inicio = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'text', 'placeholder': 'DD/MM/YYYY HH:MM'}),
        input_formats=['%d/%m/%Y %H:%M']
    )
    fecha_fin = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'text', 'placeholder': 'DD/MM/YYYY HH:MM'}),
        input_formats=['%d/%m/%Y %H:%M']
    )

    class Meta:
        model = Evento
        fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'descripcion_breve', 'imagen']

    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_inicio'].widget.attrs.update({'class': 'datetime-input'})
        self.fields['fecha_fin'].widget.attrs.update({'class': 'datetime-input'})

class SmsForm(forms.ModelForm):
    class Meta:
        model = Sms
        fields = ['tema', 'cuerpo', 'contacto']

    contacto = forms.ModelChoiceField(
        queryset=Contact.objects.all(),
        label="Contacto",
        widget=forms.Select
    )