from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json
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

def fooddetail(request, food_id):
    context = {'user_session': False,}
    nutriscore_dico = {
        "a": "/static/search/img/nutA.png",
        "b": "/static/search/img/nutB.png",
        "c": "/static/search/img/nutC.png",
        "d": "/static/search/img/nutD.png",
        "e": "/static/search/img/nutE.png"
    }

    if request.user.is_authenticated:
        context['user_session'] = True
    
    else:
        pass
    
    food = get_object_or_404(Aliment, pk=food_id)
    context['food'] = food
    for k, v in nutriscore_dico.items():
        if food.nutrition_group == k:
            context['nutriscore_img'] = v
        else:
            pass

    dico_test = {'1': 'test1', '2': 'test2', '3': 'test3'}
    context['test'] = dico_test
    context['test2'] = dict(eval(food.nutriments))

    return render(request, 'search/food_detail.html', context=context)

def savefood(request):
    req = request.POST['idFood']
    # data = json.loads(req)
    print(req)

    return JsonResponse({'ServerResponse': 'okay'})