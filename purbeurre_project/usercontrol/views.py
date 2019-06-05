from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm

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
                return redirect('index')
            else:
                context['error'] = True
    else:
        form = LoginForm()
    context['form'] = form

    return render(request, 'usercontrol/login.html', context=context)