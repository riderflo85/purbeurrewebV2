from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Aliment
from .forms import SearchForm

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

def login(request):
    return render(request, 'search/login.html')

def sign_up(request):
    return render(request, 'search/sign_up.html')

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