from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'search/index.html')

def login(request):
    return render(request, 'search/login.html')

def sign_up(request):
    return render(request, 'search/sign_up.html')

def account(request):
    return render(request, 'search/account.html')

def result(request):
    context = {
        "aliment": "Pomme de terre",
        "img": ["test"],
        "testListFood": ["Patate", "Choux", "Pomme", "Poire", "Banane", "mangue", "fraise", "framboise", "Mur", "Fruit de la passion", "Pêche", "Abricot", "Grenadine", "Ananas", "Prune", "Nectarine"],
        }
    return render(request, 'search/result.html', context)