from django.urls import path

from . import views


app_name = 'search'
urlpatterns = [
    path('', views.index, name='index'),
    path('result', views.result, name='result'),
    path('substitute/<int:food_id>', views.substitutefood, name='substitute'),
    path('food_detail/<int:pk>', views.DetailView.as_view(), name='food_detail'),
    path('mention_legale', views.legalmention, name='legal_mention'),
    path('save_food', views.savefood, name='save_food'),
    path('my_food', views.myfood, name='my_food'),
]
