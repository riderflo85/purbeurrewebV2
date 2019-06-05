from django.urls import path

from . import views

app_name = 'usercontrol'
urlpatterns = [
    path('user/signin', views.sign_in, name='user_login'),
    path('user/signup', views.sign_up, name='sign_up'),
    path('user/signout', views.sign_out, name='sign_out'),
    path('user/account', views.account, name='account'),
]
