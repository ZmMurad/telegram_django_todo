from django.http import HttpResponse
from django.shortcuts import render
from accounts.forms import UserSignUpForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
import requests
from django.contrib.auth import get_user
from dotenv import load_dotenv
import os
# Create your views here.
load_dotenv()

class UserCreationView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'sign_up.html'
    
    
def get_ac_token(request):
    if request.method=="POST":
        user=get_user(request)
        password=request.POST["password"]
        result=requests.post("http://"+os.getenv("URL_SERVER")+":"+os.getenv("PORT")+"/api/v1/auth/token/login/",data={"username":user.username,"password":password})
        result.raise_for_status()
        request.session["token"]=result.json()["auth_token"]
        return render(request,"token_account.html",{"token":result.json()["auth_token"]})
    return render(request, "token_account.html")

def delete_token(request): 
    token=request.session.get("token")
    print(token)
    result=requests.post("http://"+os.getenv("URL_SERVER")+":"+os.getenv("PORT")+"/api/v1/auth/token/logout/",headers={"Authorization":f"Token {token}"})
    result.raise_for_status()
    return render(request,"token_account.html",{"delete":"Вы удалили токен"})