from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def hellowTest(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Hacer algo después de que el formulario sea válido, como redirigir a otra página.
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})