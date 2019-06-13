from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from .models import Aliment, Favoris
from .forms import SearchForm
from .substitute import substitute

# Create your views here.
def index(request):
    context = {}
    form = SearchForm()  
    context['form'] = form

    return render(request, 'search/index.html', context=context)

def result(request):
    context = {}

    if request.method == 'POST':

        form = SearchForm(request.POST)
        if form.is_valid():
            food_search = form.cleaned_data['research']
            food = Aliment.objects.filter(name__contains=food_search)

            if food.exists():
                sub = substitute(food[0])
                context['match'] = True
                context['id'] = food[0].id
                context['name'] = food[0].name
                context['groupe_nova'] = food[0].nova_group
                context['nutrition_group'] = food[0].nutrition_group
                context['img'] = food[0].image
                context['list_food'] = sub
            
            else:
                context['match'] = False
        
        else:
            context['errors'] = form.errors.items()

        return render(request, 'search/result.html', context=context)
    
    else:
        return render(request, 'search/no_search.html', context=context)

def fooddetail(request, food_id):
    context = {}
    
    food = get_object_or_404(Aliment, pk=food_id)
    context['food'] = food
    context['nutriments'] = dict(eval(food.nutriments))

    return render(request, 'search/food_detail.html', context=context)

def savefood(request):
    req = request.POST['idFood']
    fav = Favoris()
    fav.user = request.user
    fav.substitute = Aliment.objects.get(pk=req)
    fav.save()

    return JsonResponse({'ServerResponse': 'okay'})

def myfood(request):
    context = {}
    if request.user.is_authenticated:
        food_save = Favoris.objects.filter(user=request.user.id)
        context['list_food'] = food_save

    return render(request, 'search/my_food.html', context=context)