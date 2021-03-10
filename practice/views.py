from django.shortcuts import render
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    form = UserRegistrationForm()

    return render(request, 'practice/register.html', {'form': form})
