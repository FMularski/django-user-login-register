from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user, logout


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
    form = UserLoginForm()

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login_user(request, user)
                return redirect('practice:home')
            else:
                messages.error(request, 'Invalid username or password.')

    context = {'form': form}
    return render(request, 'practice/login.html', context)


def home(request):
    return HttpResponse('home')