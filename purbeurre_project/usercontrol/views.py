from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, SignupForm

# Create your views here.
def sign_in(request):
    context = {'error': False,}

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['user']
            pwd = form.cleaned_data['password']
            user = authenticate(request, username=username, password=pwd)
            context['user'] = user

            if user is not None:
                login(request=request, user=user)
                return redirect(reverse('search:index'))
            else:
                context['error'] = True
    else:
        form = LoginForm()
    context['form'] = form

    return render(request, 'usercontrol/login.html', context=context)

def sign_up(request):
    context = {'errors': False,}

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            pseudo = form.cleaned_data['pseudo']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            pwd = form.cleaned_data['password']

            new_user = User.objects.create_user(pseudo, email, pwd)
            new_user.last_name = last_name
            new_user.first_name = first_name
            new_user.save()
            context['new_user'] = new_user

        else:
            context['errors'] = form.errors.items()

    else:
        form = SignupForm()
    context['form'] = form

    return render(request, 'usercontrol/sign_up.html', context=context)

def sign_out(request):
    logout(request)
    return render(request, 'usercontrol/sign_out.html')

def account(request):
    return render(request, 'usercontrol/account.html')