from django.urls import path

from . import views

app_name = 'search'
urlpatterns = [
    path('', views.index, name='index'),
    path('result', views.result, name='result'),
    path('food_detail/<int:food_id>', views.fooddetail, name='food_detail'),
    path('save_food', views.savefood, name='save_food'),
]
