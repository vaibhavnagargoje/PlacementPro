from django.shortcuts import render,redirect
from django.contrib.auth import login , authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.


def user_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('login_success')
        else:
            messages.error(request,"Invalid Username or Password")
    
    return render(request,'users/login.html')


def login_success(request):
    return render(request,'users/login_success.html')

def custom_logout(request):
    logout(request)
    request(request,'users/logout.html')