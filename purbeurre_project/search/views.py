from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Aliment
from .forms import SearchForm

# Create your views here.
def index(request):
    context = {'user_session': False}
    form = SearchForm()  
    context['form'] = form

    if request.user.is_authenticated:
        context['user_session'] = True

    return render(request, 'search/index.html', context=context)

def result(request):
    context = {'user_session': False,}

    if request.user.is_authenticated:
        context['user_session'] = True

    else:
        pass

    if request.method == 'POST':

        form = SearchForm(request.POST)
        if form.is_valid():
            food_search = form.cleaned_data['research']
            food = Aliment.objects.filter(name__contains=food_search)

            if food.exists():
                context['id'] = food[0].id
                context['name'] = food[0].name
                context['groupe_nova'] = food[0].nova_group
                context['nutrition_group'] = food[0].nutrition_group
                context['img'] = food[0].image
                context['list_food'] = food
        
        else:
            context['errors'] = form.errors.items()

        return render(request, 'search/result.html', context=context)
    
    else:
        return render(request, 'search/no_search.html', context=context)