from django.shortcuts import render, redirect  # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.http import HttpResponse, HttpResponseNotAllowed  # type: ignore
from django.contrib.auth import login, logout, authenticate  # type: ignore
from django.contrib.auth.decorators import login_required  # type: ignore
from .models import Contact, CampañaDeMarketing
from .forms import ContactForm, MarketingPorCorreoPersonalForm, CampañaDeMarketingForm
from .forms import Group,GroupForm
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # register user
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except:
                return render(request, 'signup.html', {'form': UserCreationForm, "error": 'username already exists!'})
        return render(request, 'signup.html', {'form': UserCreationForm, "error": 'passwords do not match!'})


def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('home')


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def marketing(request):
    if request.user.is_authenticated:
        return render(request, 'marketing.html')
    else:
        error_message = "You must be logged in to access the marketing page."
        return HttpResponseRedirect(reverse('home') + f"?error={error_message}") # type: ignore
    

@login_required
def marketing(request):
    user = request.user  # Obtenemos el usuario autenticado
    return render(request, 'marketing.html', {'user': user})

@login_required
def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marketing')
    else:
        form = ContactForm()
    return render(request, 'create_contact.html', {'form': form})

@login_required
def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return redirect('marketing')

@login_required
def view_contacts(request):
    contacts = Contact.objects.all()
    paginator = Paginator(contacts, 10)  # Muestra 10 contactos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'view_contacts.html', {'page_obj': page_obj})

@login_required
def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('view_contacts')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'create_contact.html', {'form': form})

@login_required
def create_group(request):
    message = None
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            message = 'Group created successfully!'
    else:
        form = GroupForm()
    return render(request, 'create_group.html', {'form': form, 'message': message})

@login_required
def view_groups(request):
    groups = Group.objects.all()
    return render(request, 'view_groups.html', {'groups': groups})

@login_required
def view_group_members(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    members = group.members.all()
    return render(request, 'view_group_members.html', {'group': group, 'members': members})

@login_required
def delete_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == 'POST':
        group.delete()
        return redirect('view_groups')
    return HttpResponseNotAllowed(['POST'])


@login_required
def marketing_por_email(request):
    if request.method == 'POST':
        form = MarketingPorCorreoPersonalForm(request.POST)
        if form.is_valid():
            marketing_email = form.save()
            # Enviar correo
            send_mail(
                subject=f"Nuevo {marketing_email.tipoCorreo}",
                message=marketing_email.cuerpoDelCorreo,
                from_email='your_email@example.com',
                recipient_list=[marketing_email.emailDeDestino.email],
                fail_silently=False,
            )
            return redirect('marketing')
    else:
        form = MarketingPorCorreoPersonalForm()
    return render(request, 'marketing_por_email.html', {'form': form})



@login_required
def crear_campaña_marketing(request):
    if request.method == 'POST':
        form = CampañaDeMarketingForm(request.POST)
        if form.is_valid():
            campaña = form.save(commit=False)
            grupo = campaña.grupo
            campaña.numeroDeIntegrantes = grupo.members.count()
            campaña.save()
            # Enviar correos electrónicos
            for member in grupo.members.all():
                send_mail(
                    subject=f"Nuevo {campaña.tipoCorreo}",
                    message=campaña.cuerpoDelCorreo,
                    from_email='your_email@example.com',
                    recipient_list=[member.email],
                    fail_silently=False,
                )
            return redirect('marketing')
    else:
        form = CampañaDeMarketingForm()
    return render(request, 'crear_campaña_marketing.html', {'form': form})

@login_required
def ver_campañas_marketing(request):
    campañas = CampañaDeMarketing.objects.all()
    return render(request, 'ver_campañas_marketing.html', {'campañas': campañas})

@login_required
def editar_campaña_marketing(request, campaña_id):
    campaña = get_object_or_404(CampañaDeMarketing, id=campaña_id)
    if request.method == 'POST':
        form = CampañaDeMarketingForm(request.POST, instance=campaña)
        if form.is_valid():
            form.save()
            return redirect('ver_campañas_marketing')
    else:
        form = CampañaDeMarketingForm(instance=campaña)
    return render(request, 'crear_campaña_marketing.html', {'form': form, 'editar': True})

@login_required
def eliminar_campaña_marketing(request, campaña_id):
    campaña = get_object_or_404(CampañaDeMarketing, id=campaña_id)
    campaña.delete()
    return redirect('ver_campañas_marketing')