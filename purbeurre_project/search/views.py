from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'search/index.html')

def account(request):
    return render(request, 'search/account.html')