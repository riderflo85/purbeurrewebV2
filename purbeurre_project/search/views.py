from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Aliment
from .forms import SearchForm, LoginForm, SignupForm

# Create your views here.
def index(request):
    context = {}

    if request.method == 'POST':
    #     food_search = request.POST.get('food')
    #     food = Aliment.objects.filter(name__contains=food_search)

        form = SearchForm(request.POST)
        if form.is_valid():
            food_search = form.cleaned_data['research']
            food = Aliment.objects.filter(name__contains=food_search)

            if food.exists():
                context['id'] = food[0].id
                context['name'] = food[0].name
                context['groupe_nova'] = food[0].nova_group
                context['list_food'] = food
        
        else:
            context['errors'] = form.errors.items()

        return render(request, 'search/result.html', context=context)

    else:
        form = SearchForm()  
    context['form'] = form

    return render(request, 'search/index.html', context=context)

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

    return render(request, 'search/login.html', context=context)

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

    return render(request, 'search/sign_up.html', context=context)

def sign_out(request):
    logout(request)
    return render(request, 'search/sign_out.html')

def account(request):
    return render(request, 'search/account.html')

# def result(request):
    # list_food = []
    # search = Aliment.objects.filter(name__contains=food)
    # list_food.append(search[0])

    # pour_test = ["Patate", "Choux", "Pomme", "Poire", "Banane", "mangue", "fraise", "framboise", "Mur", "Fruit de la passion", "Pêche", "Abricot", "Grenadine", "Ananas", "Prune", "Nectarine"]

    # context = {
    #     "aliment": "Aliments chercher",
    #     "img": ["test"],
    #     "testListFood": pour_test,
    #     }
    # return render(request, 'search/result.html', context)