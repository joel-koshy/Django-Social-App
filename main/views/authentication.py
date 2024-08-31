from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework import status
from ..serializers import UserSerializer 
from rest_framework.decorators import api_view
def alogin(request): 
    username=request.POST["username"]
    password=request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None: 
        login(request, user)
        return redirect("post_page")
    else: 
        return redirect("login_page")
    
def alogout(request): 
    logout(request)
    return redirect("login_page")

@api_view(['POST'])
def create_new_user(request): 
    serialized_data = UserSerializer(data=request.POST)
    if serialized_data.is_valid(): 
        serialized_data.save()
        return redirect("login_page")
    else : 
        return render(request, 'main/signup.html', {"errors":serialized_data.errors} )
