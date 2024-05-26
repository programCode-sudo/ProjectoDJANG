from django.shortcuts import render, redirect  # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.http import HttpResponse  # type: ignore
from django.contrib.auth import login, logout, authenticate  # type: ignore
from django.contrib.auth.decorators import login_required  # type: ignore

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