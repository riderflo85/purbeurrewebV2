from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, SignupForm


def sign_in(request):
    context = {'error': False,}

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['user']
            pwd = form.cleaned_data['password']
            user_log = authenticate(request, username=username, password=pwd)
            context['user'] = user_log

            if user_log is not None:
                login(request=request, user=user_log)
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
    context = {}

    if request.user.is_authenticated:
        context['pseudo'] = request.user
        context['first_name'] = request.user.first_name
        context['last_name'] = request.user.last_name
        context['email'] = request.user.email

    else:
        return redirect(reverse('usercontrol:user_login'))

    return render(request, 'usercontrol/account.html', context=context)


def change_pwd(request):
    req = request.POST
    old_pwd = req['old_pwd']
    new_pwd = req['new_pwd']
    user = request.user
    serv_response = {}

    if user.check_password(old_pwd):
        user.set_password(new_pwd)
        user.save()
        serv_response['ServerResponse'] = True
    else:
        serv_response['ServerResponse'] = False
    
    return JsonResponse(serv_response)


def change_email(request):
    req = request.POST
    old_email = req['old_email']
    new_email = req['new_email']
    user = request.user
    serv_response = {}

    if user.email == old_email:
        user.email = new_email
        user.save()
        serv_response['ServerResponse'] = True
    else:
        serv_response['ServerResponse'] = False

    return JsonResponse(serv_response)
