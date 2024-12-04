from django.shortcuts import render
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import change_password
# Create your views here.

urlpatterns= [
    path('',views.Profile,name="profile"),



    #inbuld auth routes 

    path('change-password/', change_password, name='change_password'),

]



