from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import generic
from django.contrib.auth.models import User
import json
from .models import Aliment, Favoris
from .forms import SearchForm
from .substitute import substitute


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
                context['food'] = food[0]
                context['list_food'] = sub

            else:
                context['match'] = False

        else:
            context['errors'] = form.errors.items()

        return render(request, 'search/result.html', context=context)

    else:
        return render(request, 'search/no_search.html', context=context)


def substitutefood(request, food_id):
    context = {}

    try:
        food_search = Aliment.objects.get(pk=food_id)
        sub = substitute(food_search)
        context['match'] = True
        context['food'] = food_search
        context['list_food'] = sub

    except:
        context['match'] = False

    return render(request, 'search/substitute.html', context=context)


class DetailView(generic.DetailView):
    model = Aliment
    template_name = 'search/food_detail.html'


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


def legalmention(request):
    return render(request, 'search/legal_mention.html')
