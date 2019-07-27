from django.urls import path

from . import views


app_name = 'usercontrol'
urlpatterns = [
    path('signin', views.sign_in, name='user_login'),
    path('signup', views.sign_up, name='sign_up'),
    path('signout', views.sign_out, name='sign_out'),
    path('account', views.account, name='account'),
    path('change_pwd', views.change_pwd, name='change_pwd'),
    path('change_email', views.change_email, name='change_email'),
]
