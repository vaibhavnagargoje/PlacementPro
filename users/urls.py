
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('login/',views.user_login,name='user_login'),
    path('login_success/',views.login_success,name="login_success"),
    path('logout',views.custom_logout, name="custom_logout")
]