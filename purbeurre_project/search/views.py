from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Aliment

# Create your views here.
def index(request):

    if request.method == 'POST':
        food_search = request.POST.get('food')

        food = Aliment.objects.filter(name__contains=food_search)
        if food.exists():
            context = {
                'id': food[0].id,
                'name': food[0].name,
                'groupe_nova': food[0].nova_group,
                'list_food': food,
                }
        
        return render(request, 'search/result.html', context=context)

    return render(request, 'search/index.html')

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