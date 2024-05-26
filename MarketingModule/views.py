from django.shortcuts import render  # type: ignore
from django.contrib.auth.forms import UserCreationForm  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.http import HttpResponse  # type: ignore

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
                return HttpResponse('user created success')
            except:
                return render(request, 'signup.html', {'form': UserCreationForm, "error": 'username alredy exist!'})
        return render(request, 'signup.html', {'form': UserCreationForm,"error": 'password do not match!'})
