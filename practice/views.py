from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.contrib import messages


def register(request):

    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created for ' + form.cleaned_data['username'])
            return redirect('practice:login')


    context = {'form': form}

    return render(request, 'practice/register.html', context)

def login(request):
    context = {}
    return render(request, 'practice/login.html', context)
