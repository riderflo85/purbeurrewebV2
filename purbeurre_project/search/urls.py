from django.urls import path

from . import views

app_name = 'search'
urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.sign_in, name='search_login'),
    path('signup', views.sign_up, name='sign_up'),
    path('account', views.account, name='account'),
    # path('result', views.result, name='result'),
]
